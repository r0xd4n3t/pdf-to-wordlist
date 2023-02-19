# pdf-to-wordlist
convert pdf to wordlist

# Introduction:

This code is a Python script for extracting text from PDF files and generating a list of unique words that are alphabet-only. It uses the pdfminer package to extract text from the PDF files and applies regular expressions to clean the extracted text. The resulting list of unique words is then written to a text file.

## Usage:

To use this script, you need to provide the path of the folder containing PDF files and the name of the output file. The script will then extract text from all PDF files in the folder and subfolders and write the list of unique words to the output file. You can run the script in the command line or in a Python environment.

The code can be executed in the command line as follows:

```python pdf2word.py <input-pdf-folder-path> <output-file-path>```

## Prerequisites:

This code requires the following packages to be installed:

-   pdfminer
-   tqdm

You can install these packages using pip, the Python package installer, by running the following command in the command line:

```pip install pdfminer tqdm```

Additionally, you need to have Python 3 installed on your system to run this script.
