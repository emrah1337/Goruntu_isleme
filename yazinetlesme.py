import cv2
import matplotlib.pyplot as plt

img = cv2.imread("yazi.jpg")
# bıyutlandırma
img = cv2.resize(img, (500, 600))
# gri renge dönüştürme
img_gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cl = cv2.createCLAHE(clipLimit=5)
sonuc = cl.apply(img_gri) + 30
_, ordinary_img = cv2.threshold(img_gri, 155, 255, cv2.THRESH_BINARY)
plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Orjinal img'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sonuc, cmap='gray')
plt.title('img'), plt.xticks([]), plt.yticks([])

plt.show()