
from PIL import Image
import csv
import os
import math
import pandas as pd


# Open the CSV file
csv_file = "path"

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    # Create a new list of rows with the added columns for minimum and maximum pixel values
    new_rows = []
    for row in reader:
        image = Image.open(row['DepthImage'])
        xmin, ymin, width, height = map(float, row['bbox'].split(','))
        xmax, ymax = xmin + width, ymin + height

        # Crop the image to the bounding box
        box = (xmin, ymin, xmax, ymax)
        cropped_image = image.crop(box)
        # Get the pixel values in the cropped image
        pixel_values = cropped_image.getdata()
        non_zero_pixel_values = []
        # Iterate over the pixel values and check if they're greater than 0
        for pv in pixel_values:
            if isinstance(pv, tuple):
                if pv[0] > 0:
                    non_zero_pixel_values.append(pv[0])
            elif isinstance(pv, (int, float)):
                if pv > 0:
                    non_zero_pixel_values.append(pv)
        # Get the minimum non-zero pixel value in the cropped image
        if len(non_zero_pixel_values) > 0:
            min_pixel_value = min(non_zero_pixel_values)
        else:
            min_pixel_value = 0
        # Get the maximum pixel value in the cropped image
        max_pixel_value = max(pixel_values)

        # Get the maximum pixel value in the cropped image
        mean_pixel_value = (pixel_values)

        # Add the minimum and maximum pixel values to the current row
        row['min_pixel_value'] = min_pixel_value
        row['max_pixel_value'] = max_pixel_value
        # Add the updated row to the new list of rows
        new_rows.append(row)

# Write the new rows to the CSV file
with open(csv_file, 'w', newline='') as f:
    fieldnames = reader.fieldnames + ['min_pixel_value', 'max_pixel_value']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_rows)

print ('done')




data = pd.read_csv("path")

# iterate over the rows of the DataFrame object
for index, row in data.iterrows():
    # extract the distance value from the current row
    distance = row['min_pixel_value']
    # calculate the area of the view angle using the formula
    angle_of_view = 40 # replace with the actual angle of view of your camera
    angle_in_radians = math.radians(angle_of_view)
    area_of_view_angle = (angle_in_radians / 360) * math.pi * (distance ** 2)
    # add the area of view angle to the current row
    data.at[index, 'area_of_view_angle'] = area_of_view_angle

# save the updated CSV file
data.to_csv('CameraTrapDistance_with_area.csv', index=False)


df = pd.read_csv('CameraTrapDistance_with_area.csv')

# Delete multiple columns using their column names
columns_to_delete = ['filename', 'DepthImage', 'marker', 'max_pixel_value']
df = df.drop(columns=columns_to_delete)

# Write the updated DataFrame to the CSV file
df.to_csv("CameraTrapDistanceClean.csv", index=False)
