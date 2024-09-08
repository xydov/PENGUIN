from PIL import Image, ImageTk
import customtkinter as ctk
from ttkthemes import ThemedTk
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch
import threading
import time

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
        # Change button color to blue when sending message
        send_button.configure(fg_color="#1a73e8")  # Blue color for active state
        root.after(100, lambda: send_button.configure(fg_color="#ffffff"))  # Revert to white after 100ms
        
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
            send_button.configure(fg_color="#ffffff")  # Set to white during AI response

        threading.Thread(target=generate_response).start()
    else:
        # Handle the case where no user input is provided
        send_button.configure(fg_color="#ffffff")  # Ensure button is in original state if no input

def check_input(event=None):
    """Check if there is input and update button color accordingly."""
    if input_box.get("1.0", "end-1c").strip():
        send_button.configure(fg_color="#1a73e8")  # Blue color if input is present
    else:
        send_button.configure(fg_color="#ffffff")  # White color if no input

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
    bg_image = Image.open("../pictures/eskimo.png")  # Update the path to your image
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
input_box.bind("<KeyRelease>", check_input)  # Update button color on key release

# Bind the Enter key to the send_message function
input_box.bind("<Return>", send_message)

# Send Button: To submit the input
send_button = ctk.CTkButton(root, text="SEND", width=60, height=60, command=send_message, hover_color="#1a73e8", corner_radius=120)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Set initial button color to white
send_button.configure(fg_color="#ffffff")

# Typing Label for animation
typing_label = ctk.CTkLabel(root, text="Penguin 🐧 is typing .. ", font=("Arial", 20), text_color="white", bg_color="lightblue")

# Run the main event loop
root.mainloop()

