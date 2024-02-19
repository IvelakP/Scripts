#   Author:         Paavo Mäkelä
#   File:           ReceiptReader.py
#   Description:    Simple program that reads receipts and gathers all useful information from those. The PDFs need to be converted in .txt file with 'PDFtoText.py' code

# For now the final working version, with EAN capabilities.
# TODO Check for dublicates and do something for them, check for missing EAN Codes and warn about those.

import re
import csv
import os

# Define the regular expression patterns
pattern = r'^(.*?)\s{3,}(.*?),?\s+(\d+,\d{2})\s+(\d+,\d{2})\s+(\d+)\s+(\d+)\s+(\d+,\d{2})$'
regex = r"^( {35}(?![ ])(?!.*Rahti).*)$" #Continuation pattern for description field
ean_pattern = r'\b\d{13}\b|\b\d{12}\b'  # Updated EAN regex pattern


folder_path = 'Data/'

# Create a new CSV file to store the extracted data
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['Code', 'Description', 'EAN', 'Quantity', 'Unit Price', 'Discount Percentage', 'Discount', 'Total Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the headers to the CSV file
    writer.writeheader()

    # Loop through each text file in the directory
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            # Open the text file
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                # Initialize variables to hold the fields of the current product
                code = ''
                desc = ''
                qty = 0.0
                unit_price = 0.0
                discountPercentage = 0.0
                discount = 0
                unit = 0.0
                ean = ''

                # Loop through each line in the file
                for line in f:
                    # Try to match the pattern to the line
                    match = re.match(pattern, line)
                    match1 = re.match(regex, line)
                    ean_match = re.search(ean_pattern, line)

                    if match:
                        # If the previous product has been processed, add its details to the CSV file
                        if code:
                            writer.writerow({'Code': code, 'Description': desc, 'EAN': ean, 'Quantity': qty, 'Unit Price': unit_price, 'Discount Percentage': discountPercentage, 'Discount': discount, 'Total Price': unit})

                        # Extract the fields from the matched groups and assign them to the variables
                        code = match.group(2)[:10]
                        desc = match.group(2)[10:].strip()
                        qty = float(match.group(3).replace(',', '.'))
                        unit_price = float(match.group(4).replace(',', '.'))
                        discountPercentage = float(match.group(5).replace(',', '.'))
                        discount = int(match.group(6))
                        unit = float(match.group(7).replace(',', '.'))
                        ean = ''
                    elif ean_match:
                        # Extract the EAN code from the line
                        ean = ean_match.group(0)
                    elif match1:
                        # Combine the current description with the previous one
                        desc += f' {match1.group(1).strip()}'

                # Add the details of the last product in the file to the CSV file
                if code:
                    writer.writerow({'Code': code, 'Description': desc, 'EAN': ean, 'Quantity': qty, 'Unit Price': unit_price, 'Discount Percentage': discountPercentage, 'Discount': discount, 'Total Price': unit})
