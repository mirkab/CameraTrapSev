import cv2
import os

# set the input and output folder paths
input_folder = "Path"
output_folder = "DepthImageEdit"

# create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through all files in the input folder
for filename in os.listdir(input_folder):
    # load the image and create a mask for zero and over 35 values
    img_path = os.path.join(input_folder, filename)
    img = cv2.imread(img_path, cv2.IMREAD_ANYDEPTH)
    mask_zero = img == 0
    mask_over_35 = img > 35

    # set pixel values to 99 according to the masks
    img[mask_zero] = 99
    img[mask_over_35] = 99

    # set the bottom row of pixels to 0
    img[-1, :] = 0

    # save the modified image to the output folder
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, img)