import customtkinter as ctk
from ttkthemes import ThemedTk
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import torch  # Make sure to import torch for no_grad context
import threading
import time

# Load the Blenderbot model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def my_AI_Answer(input_text):
    """Generate a response from the AI model based on the input text."""
    # Disable gradient calculation for model inference
    with torch.no_grad():
        inputs = tokenizer(input_text, return_tensors="pt")
        reply_ids = model.generate(**inputs)
        reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return reply

def display_typing_animation():
    """Show a typing animation in the chat window."""
    typing_label.grid(row=2, column=0, columnspan=2, pady=5, sticky="nsew")  # Use grid instead of pack
    for dot in range(4):
        typing_label.configure(text="Penguin  is  typing" + "." * dot)
        time.sleep(1)
    typing_label.grid_forget()

def send_message(event=None):  # event=None is required to handle both button click and Enter key press
    """Handles sending the message and displaying the response."""
    user_input = input_box.get("1.0", "end-1c").strip()  # Correctly get input from the text box without extra newlines
    if user_input:
        chat_history.configure(state=ctk.NORMAL)  # Enable the chat history to update it
        chat_history.insert(ctk.END, f"You: {user_input}\n")  # Display user message
        chat_history.see(ctk.END)  # Auto-scroll to the bottom
        input_box.delete("1.0", ctk.END)  # Clear the input box after sending the message
        
        # Typing animation before showing response
        animation_thread = threading.Thread(target=display_typing_animation)
        animation_thread.start()
        
        # Generate AI response after a delay (simulating AI typing time)
        def generate_response():
            try:
                bot_response = my_AI_Answer(user_input)
                animation_thread.join()  # Ensure animation is complete
                chat_history.insert(ctk.END, f"Penguin AI : {bot_response}\n")  # Display bot response
                chat_history.see(ctk.END)  # Auto-scroll to the bottom
                chat_history.configure(state=ctk.DISABLED)  # Disable chat history to make it read-only
            except Exception as e:
                chat_history.insert(ctk.END, f"Error: {str(e)}\n")
                chat_history.see(ctk.END)

        threading.Thread(target=generate_response).start()

# Create the main window with a modern look
root = ThemedTk(theme="breeze")
root.title("Penguin 🐧")
root.geometry("600x500")

# Set theme mode for customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (auto), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Available themes: "blue", "green", "dark-blue"

# Configure the grid layout to expand
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)
root.grid_rowconfigure(2, weight=0)

# Chat History: Scrolled text box
chat_history = ctk.CTkTextbox(root, wrap=ctk.WORD, state=ctk.DISABLED, font=("Arial", 20), text_color="white", bg_color="darkblue")
chat_history.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

# User Input Box: For typing messages
input_box = ctk.CTkTextbox(root, height=40, font=("Arial", 20), text_color="white", bg_color="lightgrey")
input_box.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Bind the Enter key to the send_message function
input_box.bind("<Return>", send_message)

# Send Button: To submit the input
send_button = ctk.CTkButton(root, text="Send", width=80, command=send_message, hover_color="#1a73e8", corner_radius=9)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Typing Label for animation
typing_label = ctk.CTkLabel(root, text="Penguin 🐧 is typing .. ", font=("Arial", 20), text_color="white", bg_color="darkorange")

# Run the main event loop
root.mainloop()

