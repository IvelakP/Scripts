#   Author:         Paavo Mäkelä
#   File:           ProductReader.py
#   Description:    Simple program that reads json files and extracts wanted properties to csv


# Imports
import json
import csv
import os

# Directory containing the JSON files
directory = "Asemat/"

# CSV file path to save the extracted data
csv_file = "Products.csv"

# List to store the extracted data
data_list = []

# Iterate over the files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        file_path = os.path.join(directory, filename)

        # Open and load the JSON file
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Extract all the wanted things from json files
            eans = data.get("eans", [])
            description = data.get("description", "")
            description_short = data.get("descriptionShort", "")
            images = data.get("images", [])
            rating = data.get("rating", "")
            mpns = data.get("mpns", [])
            category = data.get("category", [])
            brand = data.get("brand", "")

            # Combine multiple EANs into one cell separated by commas
            ean_string = ", ".join(eans)

            # Append the extracted data to the list
            data_list.append([ean_string, description, description_short, images, rating, mpns, category, brand])

# Save the extracted data to a CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ean", "description", "descriptionShort", "images", "rating", "mpns", "category", "brand"])  # Write the header
    writer.writerows(data_list)  # Write the data rows

print("CSV file created successfully.")
