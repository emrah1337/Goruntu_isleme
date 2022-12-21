import cv2
import numpy as np

img = cv2.imread('aracplakasi.jpg', 0).astype(float) // 255


kenar = [[0,1,0],[1,1,1],[0,1,0]]
dil = img.copy()


for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        pixel = img[i - 1][j] * kenar[0][1] + img[i][j - 1] * kenar[1][0] + img[i][j] * kenar[1][1] + img[i][j + 1] * kenar[1][2] + img[i + 1][j] * kenar[2][1] 
        if pixel > 0:
            dil[i][j] = 1
        else:
            dil[i][j] = 0


masked = cv2.bitwise_xor(img,dil,mask = None)

cv2.imshow('Original', img)
cv2.imshow('Kenar', masked)
cv2.waitKey(0)
cv2.destroyAllWindows()