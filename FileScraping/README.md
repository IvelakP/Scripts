# README for FileScraping folder

## PDFtoText.py

This file converts PDF files to text files using "ghostscripts". Only tested in Ubuntu (WSL) environment and most likely won't work in other environments.

## PDFtoWORD.py

Work in progress...

## ProducReader.py

Reads JSON files and extracts trhe hard coded details and places details to CSV file.

## ReceiptReader.py

Reads data from receipts after they have been converted from PDF to txt using the "PDFtoText.py". Places the extracted data to CSV file.
Currently seeks for EAN and then adds all relevant information for that EAN to CSV.
