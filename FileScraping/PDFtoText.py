#       Author:         Paavo Mäkelä
#       File:           PDFtoText.py
#       Description:    Simple script that transforms PDF files to text files in Linux environment, using ghostscript

# Tested only in Linux (Ubuntu) environment
# sudo apt-get -y install ghostscript

import os

# Set the path to the folder containing the PDF files
pdf_folder = 'Data'

# Loop through each PDF file in the folder
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith('.pdf'):
        # Generate the output text file name
        txt_file = os.path.join(pdf_folder, os.path.splitext(pdf_file)[0] + '.txt')

        # Run the Ghostscript command to convert the PDF to text
        cmd = f'gs -sDEVICE=txtwrite -o "{txt_file}" "{os.path.join(pdf_folder, pdf_file)}"'
        os.system(cmd)