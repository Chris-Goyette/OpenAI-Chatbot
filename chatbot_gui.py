import tkinter as tk

# Initialize the Tkinter window
root = tk.Tk()
root.title("My GPT-3.5 Chatbot")
root.geometry("500x500")

# Text widget for chat history
chat_history = tk.Text(root, width=60, height=20)
chat_history.grid(row=0, column=0, columnspan=2)

# Entry widget for user input
user_input = tk.Entry(root, width=60)
user_input.grid(row=1, column=0)

# Button to send message
send_button = tk.Button(root, text="Send", width=10)
send_button.grid(row=1, column=1)

# Run the Tkinter event loop
root.mainloop()
