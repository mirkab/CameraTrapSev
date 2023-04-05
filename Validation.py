import os
import shutil
import pandas as pd

os.chdir("path")

# Define the CSV file path
csv_file_path = "path"

# Define the path of the new directory to copy the validation images
validation_dir = "path"

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Get the rows where the value of the 'validation' column is 'yes'
validation_rows = df.loc[df['marker'] == 'yes']

# Create the validation directory if it doesn't exist
if not os.path.exists(validation_dir):
    os.mkdir(validation_dir)

# Loop through the rows and copy the images to the validation directory
for index, row in validation_rows.iterrows():
    image_path = row['filename']
    image_filename = os.path.basename(image_path)
    validation_path = os.path.join(validation_dir, image_filename)
    print (image_path)
    shutil.copy2(image_path, validation_path)

print('Validation images have been copied successfully.')