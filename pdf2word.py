import re
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
from tqdm import tqdm

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text

folder_path = input("Enter the path of the folder containing pdfs: ")
output_file_name = input("Enter the name of the output file: ")

# Get a list of all pdf files in the folder and subfolders
pdf_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(root, file))

# Open the text file for writing
with open(output_file_name, "w") as f:
    # List to store problematic PDF files
    problematic_files = []
    # Iterate over each pdf file
    for pdf_file in tqdm(pdf_files, desc="Extracting text from pdf"):
        try:
            text = convert_pdf_to_txt(pdf_file)
        except:
            # Handle any errors that occur, such as the one you provided
            print("Error processing", pdf_file)
            problematic_files.append(pdf_file)
            continue
        # Strip all the new lines and whitespaces
        text = text.replace('\n', ' ')

        # remove special characters from the text
        text = re.sub('[^A-Za-z0-9]+', ' ', text)

        # Extract the words and remove the words containing numbers 
        words = [word for word in text.split() if word.isalpha()]

        # remove duplicates and sort
        words = sorted(list(set(words)))

        # Write the words to the text file
        for word in words:
            f.write(word + '\n')
    # Print out the problematic PDF files
    if problematic_files:
        print("The following PDF files caused errors:")
        for file in problematic_files:
            print(file)            
with open(output_file_name, "r") as f:
    # Read the words from the file
    words = f.read().splitlines()

# remove duplicates and sort
words = sorted(list(set(words)))

with open(output_file_name, "w") as f:
    # Write the words to the text file
    for word in tqdm(words, desc="Cleaning up output file"):
        f.write(word + '\n')
