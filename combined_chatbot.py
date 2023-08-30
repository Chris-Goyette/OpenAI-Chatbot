import os
import tkinter as tk
import openai

# Fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the Tkinter window
root = tk.Tk()
root.title("My GPT-3.5 Chatbot")
root.geometry("700x500")

# Text widget for chat history
chat_history = tk.Text(root, width=60, height=20)
chat_history.grid(row=0, column=0, columnspan=2)

# Entry widget for user input
user_input = tk.Entry(root, width=60)
user_input.grid(row=1, column=0)

# Function to handle button click
def send_message():
    user_message = user_input.get()
    chat_history.insert(tk.END, f"You: {user_message}\n")
    user_input.delete(0, tk.END)

    # Prepare a list of messages
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message},
    ]

    # Make a chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Print the assistant's reply
    bot_message = response['choices'][0]['message']['content']
    chat_history.insert(tk.END, f"Bot: {bot_message}\n")

# Button to send message
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1)

# Run the Tkinter event loop
root.mainloop()
