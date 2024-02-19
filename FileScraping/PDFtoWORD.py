import os
from pdf2docx import Converter #pip install pdf2docx

# Set the path to the folder containing the PDF files
pdf_folder = 'Data'

# Loop through each PDF file in the folder
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith('.pdf'):
        # Generate the output Word file name
        docx_file = os.path.join(pdf_folder, os.path.splitext(pdf_file)[0] + '.docx')

        # Use pdftotext to extract text from the PDF
        txt_file = os.path.join(pdf_folder, os.path.splitext(pdf_file)[0] + '.txt')
        cmd = f'pdftotext "{os.path.join(pdf_folder, pdf_file)}" "{txt_file}"'
        os.system(cmd)

        # Use pdf2docx to convert the text file to a Word document
        cv = Converter(txt_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()

        # Optionally, you can remove the intermediate text file
        os.remove(txt_file)
