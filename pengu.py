import tkinter as tk
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load the model and tokenizer
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def my_AI_Answer(input_text):
    """Generate a response from the AI model based on the input text."""
    inputs = tokenizer(input_text, return_tensors="pt")
    reply_ids = model.generate(**inputs)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return reply

def send_message():
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        root.quit()
    else:
        response = my_AI_Answer(user_input)
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_input}\n")
        chat_log.insert(tk.END, f"Penguin AI: {response}\n")
        chat_log.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)
        chat_log.yview(tk.END)

# Create the main window
root = tk.Tk()
root.title("Penguin AI Chat")

# Create a chat log area
chat_log = tk.Text(root, height=20, width=50, state=tk.DISABLED)
chat_log.pack(padx=10, pady=10)

# Create a user input area
user_entry = tk.Entry(root, width=50)
user_entry.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=5, side=tk.RIGHT)

# Run the application
root.mainloop()

