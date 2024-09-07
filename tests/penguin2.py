import tkinter as tk
from PIL import Image, ImageTk
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import os
import platform
import threading

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def my_AI_Answer(input_text):
    """Generate a response from the AI model based on the input text."""
    try:
        inputs = tokenizer(input_text, return_tensors="pt")
        reply_ids = model.generate(**inputs)
        reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
        return reply
    except Exception as e:
        return f"Error generating response: {e}"

def clear_console():
    """Clear the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def send_message(event=None):
    """Send message and display response."""
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        root.quit()
    elif user_input.lower() == 'clear':
        clear_console()
        chat_log.config(state=tk.NORMAL)
        chat_log.delete(1.0, tk.END)
        chat_log.config(state=tk.DISABLED)
    else:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_input}\n")
        chat_log.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)
        chat_log.yview(tk.END)
        
        # Start a new thread to handle the long-running AI response
        response_thread = threading.Thread(target=handle_response, args=(user_input,))
        response_thread.start()

def handle_response(user_input):
    """Handle AI response in a separate thread."""
    response = my_AI_Answer(user_input)
    # Update the chat log with the response in the main thread
    root.after(0, update_chat_log, response)

def update_chat_log(response):
    """Update the chat log with the AI response."""
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"Penguin AI: {response}\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Penguin AI Chat")

# Set window size and position
root.geometry("800x600")  # Adjust to fit your background image size

# Load and set the background image
try:
    bg_image = Image.open("../pictures/logo-color.png")
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Ensure the image fits the window
    bg_photo = ImageTk.PhotoImage(bg_image)
    
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")

# Create a frame for the chat log and user input
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

# Create a chat log area within the frame
chat_log = tk.Text(frame, height=20, width=50, state=tk.DISABLED, bg='white', fg='black')
chat_log.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a user input area within the frame
user_entry = tk.Entry(frame, width=50)
user_entry.pack(side=tk.LEFT, fill=tk.X, padx=5, pady=5)

# Create a send button within the frame
send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

# Bind the Enter key to the send_message function
user_entry.bind('<Return>', send_message)

# Run the application
root.mainloop()

