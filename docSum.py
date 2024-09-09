#!/usr/bin/env python3

import os
from posixpath import split  # Importing the os module to interact with environment variables
from groq import Groq  # Importing the Groq class from the groq package


def split_document_into_chunks(text):
    r'''
    Split input text into smaller chunks so that the LLM can process the chunks individually.

    >>> split_document_into_chunks('This is a sentence.\n\nThis is another paragraph.')
    ['This is a sentence.', 'This is another paragraph.']
    
    >>> split_document_into_chunks('First paragraph.\n\nSecond paragraph.\n\nThird paragraph.')
    ['First paragraph.', 'Second paragraph.', 'Third paragraph.']
    
    >>> split_document_into_chunks('Single paragraph with no breaks.')
    ['Single paragraph with no breaks.']
    
    >>> split_document_into_chunks('Empty string test.\n\n')
    ['Empty string test.', '']
    '''
    
    return text.split('\n\n')


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
with open(args.filename, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    
# Function to split the document into paragraphs
paragraphs = split_document_into_chunks(text)

# print(len(paragraphs)) 

while(len(paragraphs) > 1):
    tmp_text = []  # List to store the summarized paragraphs
    for paragraph in paragraphs:
        
        # Create a chat completion using the Groq API, sending a system instruction and the user input
        # print('hi')
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'system',  
                    'content': 'Summarize the input text below. Limit the summary to 1 paragraph.'
                },
                {
                    'role': 'user',  # Indicating the user's role in the conversation
                    'content': paragraph,  # Passing the content of the file as the user's input
                }
            ],
            model="llama3-8b-8192",  # Specifying the model to use for generating the summary
        )

        # Append the summarized content to the list
        tmp_text.append(chat_completion.choices[0].message.content)

    # Join all summarized paragraphs into a single string
    summarized_text = ''.join(tmp_text)

    # Re-split the summarized text into paragraphs
    paragraphs = split_document_into_chunks(summarized_text)
    # print(len(paragraphs))  


print(paragraph)



