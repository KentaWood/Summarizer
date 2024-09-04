
# Document Summarizer using Groq AI

This project uses the Groq AI API to summarize text documents. You can easily run the script from the terminal to get a summary of a specified document.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install groq
   ```

2. **Set Groq API Key**:
   Store your Groq API key in an environment variable:
   ```bash
   export GROQ_API_KEY="your-groq-api-key"
   ```

## Usage (Can only process upto 30000 Tokens ~ 20000-25000 Words)

To summarize a document, run:

```bash
python3 docSummary.py declaration
```

Replace `declaration` with the name of your text file. 

## Brief Overview

The script reads the content of the specified file, sends it to the Groq model for summarization, and prints the summary in the terminal.

```

This version gives a quick overview of the project and instructions on how to set it up and use it.
