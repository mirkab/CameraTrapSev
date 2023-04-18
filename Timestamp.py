import csv
from PIL import Image
import os

# Set the directory containing the input CSV file and image files
input_dir = 'C:/Users/Blair Mirka/Documents/UNM_Ph.D/CameraTrap'
image_dir = 'C:/Users/Blair Mirka/Documents/UNM_Ph.D/CameraTrap'

# Set the directory to store the output CSV file
output_dir = 'C:/Users/Blair Mirka/Documents/UNM_Ph.D/CameraTrap'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Construct the absolute path to the input CSV file
input_file = os.path.join(input_dir, 'CameraTrapLabels_20230207.csv')

# Construct the absolute path to the output CSV file
output_file = os.path.join(output_dir, 'timestamps.csv')

# Open the input CSV file containing the file paths
with open(input_file, 'r') as csvfile:
    # Read the CSV file using csv.DictReader
    reader = csv.DictReader(csvfile)

    # Create a new CSV file to store the timestamps
    with open(output_file, 'w', newline='') as outfile:
        # Define the fieldnames for the output CSV file
        fieldnames = ['file_path', 'timestamp']

        # Create a csv.DictWriter object to write to the output CSV file
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Write the header row to the output CSV file
        writer.writeheader()

        # Loop through each row in the input CSV file
        for row in reader:
            # Extract the file path from the current row
            file_path = os.path.join(image_dir, row['filename'])

            # Construct the absolute path to the image file
            image_file = os.path.join(input_dir, file_path)

            # Open the image file and extract the EXIF data
            with Image.open(image_file) as img:
                exif_data = img._getexif()

            # Extract the timestamp from the EXIF data
            timestamp = exif_data.get(36867)

            # Write the file path and timestamp to the output CSV file
            writer.writerow({'file_path': file_path, 'timestamp': timestamp})
