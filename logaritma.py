import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("picture1.jpg")
gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# uzun
# print(resim.shape) # (axb) boyutlari
# for i in range(600):
#     for j in range(800):
#         # print(resim[i,j])
#         resim[i,j] = 5*log(resim[i,j]+1,10) #
#
c = 50  # formulde c sabit

formul = c * (np.log(gray + 1))
logarithm = np.array(formul, dtype=np.uint8)

cv2.imshow("Original", resim)
cv2.imshow("logarithm", logarithm)
#plt.imshow(logarithm)
#plt.show(logarithm)
cv2.waitKey(0)
cv2.destroyAllWindows()
