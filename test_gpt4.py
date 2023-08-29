
import os
import openai

# Fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client
openai.api_key = api_key

# Prepare a list of messages. The first message is from the user,
# and the second message is from the assistant. The user's message
# sets the behavior of the assistant, and the assistant's message
# generates a response based on the user's message.
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "If I made changes to my .zshrc file in VS code and save the changes, will my updates take effect?"},
]

# Make a chat completion request
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or whatever chat model you have access to
    messages=messages
)

# Print the assistant's reply
print(response['choices'][0]['message']['content'])


