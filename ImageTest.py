import cv2

img_path = "Path"
img = cv2.imread(img_path, cv2.IMREAD_ANYDEPTH)

# find the minimum, maximum, and average values
(min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(img)
(avg_val, _, _, _) = cv2.mean(img)

# print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print("Average value:", avg_val)