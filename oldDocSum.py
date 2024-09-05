import os
from posixpath import split  # Importing the os module to interact with environment variables
from groq import Groq  # Importing the Groq class from the groq package


# parse command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# Initialize the Groq client using an API key retrieved from environment variables
client = Groq(
    # Retrieve the API key from the environment, assuming it is stored in an environment variable 'GROQ_API_KEY'
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Open the file in read mode and store its content in the variable 'text'
with open(args.filename) as f:
    text = f.read()

'''
We need to call the split func onto the text
Then fpr each paragrapgh in the outpult list,call the LLM code belwowe to sumarzie it Put the sumary int o a new list
Recall the LLM code Below on the new smaller
'''


# Create a chat completion using the Groq API, sending a system instruction and the user input
chat_completion = client.chat.completions.create(
    messages=[
        {
            'role': 'system',  
            'content': 'Summarize the input text below. Limit the summary to 1 paragraph.'
        },
        {
            "role": "user",  # Indicating the user's role in the conversation
            "content": text,  # Passing the content of the file as the user's input
        }
    ],
    model="llama3-8b-8192",  # Specifying the model to use for generating the summary
)

# Print the content of the first choice returned by the model i.e. the SUMMARY
print(chat_completion.choices[0].message.content)
