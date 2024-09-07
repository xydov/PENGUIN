from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import os
import platform

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

def clear_console():
    """Clear the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# ANSI escape codes for colors
LIGHT_BLUE = "\033[94m"
LIGHTER_BLUE = "\033[96m"
RESET_COLOR = "\033[0m"

# Print welcome message in light blue
print(f"{LIGHT_BLUE}Welcome to the Penguin AI chat! Type 'exit' to quit. Type 'clear' to clear the conversation.{RESET_COLOR}")

while True:
    # Get user input with a light blue arrow
    user_input = input(f"{LIGHT_BLUE}---> {RESET_COLOR}")
    
    # Check for exit condition
    if user_input.lower() == 'exit':
        print("Exiting...")
        break
    
    # Check for clear command
    if user_input.lower() == 'clear':
        clear_console()
        print(f"{LIGHT_BLUE}Welcome to the Penguin AI chat! Type 'exit' to quit. Type 'clear' to clear the conversation.{RESET_COLOR}")
        continue
    
    # Generate and print AI response
    response = my_AI_Answer(user_input)
    print(f"{LIGHTER_BLUE}Penguin AI 🐧{RESET_COLOR}:")
    print(response)

