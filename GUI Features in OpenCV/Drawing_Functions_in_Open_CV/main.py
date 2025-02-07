"""
In all the above functions, you will see some common arguments as given below:

img : The image where you want to draw the shapes
color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.
"""

import numpy as np
import cv2 as cv
 
# Create a black image
img = np.zeros((512,512,3), np.uint8)
 
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)

# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. This time we will draw a green rectangle at the top-right corner of image.
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Drawing Circle: To draw a circle, you need its center coordinates and radius. We will draw a circle inside the rectangle drawn above.
cv.circle(img,(447,63), 63, (0,0,255), -1)

# Draw Ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Draw Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

cv.imshow('draw image', img)

cv.waitKey(0)
cv.destroyAllWindows()