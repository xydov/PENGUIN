from PIL import Image, ImageTk
import customtkinter as ctk
from ttkthemes import ThemedTk
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch
import threading
import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the Blenderbot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def my_AI_Answer(input_text):
    """Generate a response from the AI model based on the input text."""
    with torch.no_grad():
        inputs = tokenizer(input_text, return_tensors="pt")
        reply_ids = model.generate(**inputs)
        reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return reply

def display_typing_animation():
    """Show a typing animation in the chat window."""
    typing_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="nsew")
    for dot in range(4):
        typing_label.configure(text="Penguin is typing" + "." * dot)
        time.sleep(1)
    typing_label.grid_forget()

def send_message(event=None):
    """Handles sending the message and displaying the response."""
    user_input = input_box.get("1.0", "end-1c").strip()
    if user_input:
        # Animate the button click
        send_button.configure(fg_color="#1a73e8")  # Change color to indicate click
        root.after(100, lambda: send_button.configure(fg_color="#ffffff"))  # Revert color after 100ms
        
        chat_history.configure(state=ctk.NORMAL)
        chat_history.insert(ctk.END, f"You: {user_input}\n")
        chat_history.see(ctk.END)
        input_box.delete("1.0", ctk.END)
        
        # Typing animation before showing response
        animation_thread = threading.Thread(target=display_typing_animation)
        animation_thread.start()
        
        # Generate AI response after a delay
        def generate_response():
            try:
                bot_response = my_AI_Answer(user_input)
                animation_thread.join()
                chat_history.insert(ctk.END, f"Penguin AI : {bot_response}\n")
                chat_history.see(ctk.END)
                chat_history.configure(state=ctk.DISABLED)
            except Exception as e:
                chat_history.insert(ctk.END, f"Error: {str(e)}\n")
                chat_history.see(ctk.END)
            
            # Revert button color after AI response is added
            send_button.configure(fg_color="#1a73e8")  # Original color

        threading.Thread(target=generate_response).start()
    else:
        # Handle the case where no user input is provided
        send_button.configure(fg_color="#1a73e8")  # Ensure button is in original state if no input

def play_startup_sound():
    """Play the startup sound in a separate thread."""
    pygame.mixer.music.load("../sounds/rain.mp3")  # Update the path to your sound file
    pygame.mixer.music.play(-1)  # Play the sound in a loop

def stop_startup_sound():
    """Stop the startup sound."""
    pygame.mixer.music.stop()

# Create the main window
root = ThemedTk(theme="breeze")
root.title("Penguin 🐧")
root.geometry("600x500")

# Set theme mode for customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Configure the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

# Create a canvas to hold the background image
canvas = ctk.CTkCanvas(root, bg='lightgrey')
canvas.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")
canvas.grid_rowconfigure(0, weight=1)
canvas.grid_columnconfigure(0, weight=1)

# Load and display the background image
try:
    bg_image = Image.open("../pictures/logo-color.png")  # Update the path to your image
    bg_image = bg_image.resize((600, 500), Image.Resampling.LANCZOS)  # Use Resampling.LANCZOS for resizing
    bg_photo = ImageTk.PhotoImage(bg_image)
    canvas.create_image(0, 0, image=bg_photo, anchor='nw')
    canvas.image = bg_photo  # Keep a reference to the image
except Exception as e:
    print(f"Error loading image: {e}")

# Chat History: Scrolled text box
chat_history = ctk.CTkTextbox(root, wrap=ctk.WORD, state=ctk.DISABLED, font=("Arial", 20), text_color="white", bg_color="transparent")
chat_history.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

# User Input Box: For typing messages
input_box = ctk.CTkTextbox(root, height=40, font=("Arial", 20), text_color="white", bg_color="lightgrey")
input_box.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Bind the Enter key to the send_message function
input_box.bind("<Return>", send_message)

# Send Button: To submit the input
send_button = ctk.CTkButton(root, text="Send", width=120, height=50, command=send_message, hover_color="#1a73e8", corner_radius=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Typing Label for animation
typing_label = ctk.CTkLabel(root, text="Penguin is typing .. ", font=("Arial", 20), text_color="white", bg_color="darkorange")

# Play sound on application launch
startup_sound_thread = threading.Thread(target=play_startup_sound)
startup_sound_thread.start()

# Stop the startup sound when the application is closed
def on_closing():
    stop_startup_sound()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main event loop
root.mainloop()

