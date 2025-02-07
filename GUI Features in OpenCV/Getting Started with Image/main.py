import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
 
img = cv.imread('input.png')
 
if img is None:
    sys.exit("Could not read the image.")
 
print(img.shape)

RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(RGB_img)
plt.waitforbuttonpress()
plt.close('all')

cv.imshow("Display window", img)
k = cv.waitKey(0)
 
if k == ord("s"):
    cv.imwrite("output.png", img)
 