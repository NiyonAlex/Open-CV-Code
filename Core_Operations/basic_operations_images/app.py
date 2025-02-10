import numpy as np
import cv2 as cv

img = cv.imread('roi.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

# accessing image pixel value
print(img[100, 30]) # access pixel point x = 100, y = 30
print(img[100, 30, 2]) # access red point of pixel 100, 30

# Acess Image Properties
print('image shape: ' + img.shape)
print('image size:' + img.size)
print('image datatype: ' + img.dtype)

# Image ROI
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# Channels
b,g,r = cv.split(img)
img = cv.merge((b,g,r))

# b = img[:,:,0] # blue color
# img[:,:,2] = 0 # remove red channel

