import csv
from PIL import Image

image_path = "path"
image = Image.open(image_path)
image = Image.open(image_path)
pixel_values = list(image.getdata())
min_pixel_value = min(pixel_values)
max_pixel_value = max(pixel_values)
print('Minimum pixel value:', min_pixel_value)
print('Maximum pixel value:', max_pixel_value)
