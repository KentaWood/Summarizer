[![tests](https://github.com/KentaWood/Summarizer/actions/workflows/tests.yml/badge.svg)](https://github.com/KentaWood/Summarizer/actions/workflows/tests.yml)

# Document Summarizer using Groq AI

This project utilizes the Groq AI API to summarize text documents. You can easily run the script from the terminal to generate a summary of a specified document.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install groq
   ```

2. **Set Groq API Key as an Environment Variable**:
   To set up the environment variable, activate the virtual environment and export the `.env` file:

   ```bash
   source venv/bin/activate
   export $(cat .env)
   ```

## Usage

To summarize a document, run the following command:

```bash
python3 docSummary.py <filename>
```

Replace `<filename>` with the name of the text file you want to summarize.

## Brief Overview

The script reads the content of the specified file, sends it to the Groq model for summarization, and prints the summary in the terminal.
