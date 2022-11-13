import cv2
import numpy as np


# Read the image and convert it to gray
resim = cv2.imread("picture1.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

X = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
Y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
XY = X + Y

cv2.imshow("Original", resim)
cv2.imshow("X", X)
cv2.imshow("Y", Y)
cv2.imshow("X+Y", XY)

cv2.waitKey(0)
cv2.destroyAllWindows()
