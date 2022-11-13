import cv2
import numpy as np

resim = cv2.imread("picture1.jpg", cv2.IMREAD_GRAYSCALE)

kernelX = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernelY = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

PrewittX = cv2.filter2D(resim, -1, kernelX)
PrewittY = cv2.filter2D(resim, -1, kernelY)

cv2.imshow("Original", resim)
cv2.imshow("PrewittX", PrewittX)
cv2.imshow("PrewittY", PrewittY)
cv2.imshow("PrewittX+Y", PrewittX+PrewittY)

cv2.waitKey(0)
cv2.destroyAllWindows()
