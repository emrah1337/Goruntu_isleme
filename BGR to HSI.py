import cv2
import numpy as np
import math

img = cv2.imread("aracplakasi.jpg")

bgr_renkleri = np.float32(img) / 255

mavi = bgr_renkleri[:, :, 0]
yesil = bgr_renkleri[:, :, 1]
kirmizi = bgr_renkleri[:, :, 2]

intensity = np.divide(mavi + yesil + kirmizi, 3)

minimum = np.minimum(np.minimum(kirmizi, yesil), mavi)
saturation = 1 - (3 / (kirmizi + yesil + mavi + 0.001) * minimum)

hue = np.copy(mavi)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        hue[i][j] = 0.5 * ((kirmizi[i][j] - yesil[i][j]) + (kirmizi[i][j] - mavi[i][j])) / math.sqrt(
            (kirmizi[i][j] - yesil[i][j]) ** 2 + ((kirmizi[i][j] - mavi[i][j]) * (yesil[i][j] - mavi[i][j])))

        hue[i][j] = math.acos(hue[i][j])

        if mavi[i][j] <= yesil[i][j]:
            hue[i][j] = hue[i][j]
        else:
            hue[i][j] = ((360 * math.pi) / 180.0) - hue[i][j]

hsi_img = cv2.merge((hue, saturation, intensity))

cv2.imshow("gercekresim", img)
cv2.imshow("HSI", hsi_img)

cv2.waitKey(0)
cv2.destroyAllWindows()