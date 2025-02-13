import numpy as np
import cv2 as cv

e1 = cv.getTickCount()
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)

img1 = cv.imread('messi5.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"

e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)

cv.useOptimized()
res = cv.medianBlur(img, 49)
print(res)
cv.setUseOptimized(False)

cv.useOptimized()

res = cv.medianBlur(img, 49)

z = cv.countNonZero(img)

z = cv.np.count_nonzero(img)