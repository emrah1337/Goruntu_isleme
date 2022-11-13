import cv2
import numpy as np

resim = cv2.imread('gamma.jpg')
c=1 #slaytta tüm durumlarda c=1 yazıyor
for gamma in [3, 4, 5]:
    cvt = c * np.array(resim ** gamma, dtype = 'uint8')
    cv2.imshow('yeni' + str(gamma) + '.jpg', cvt)




# resim = cv2.imread("picture1.jpg",0)
# # graycvt = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) 4. satır ile aynı mantık
#
# # print(resim.shape) # boyutlarını yazdırıyoruz, iki tane deger vericek (satir(img_1.shape[0]) sutun(img_1.shape[1]))
# c = 1
# formul =
# resim_gama = np.power(resim, formul).clip(0, 255).astyppe(np.uint8)
#
# for i in range(img_1.shape[0]):
#     for j in range(img_1.shape[1]):
#         img_1[i,j] = c * img_1[i,j] ** 3
#
# gamma = 3
# img_2 = c * np.power(img_1, gamma)
#
# gamma = 4
# img_3 = c * np.power(img_1, gamma)
#
# gamma = 5
# img_4 = c * np.power(img_1, gamma)
#
# cv2.imshow("Original", img_1)
# cv2.imshow("Gamma 3", img_2)
# cv2.imshow("Gamma 4", img_3)
# cv2.imshow("Gamma 5", img_4)

cv2.waitKey(0)
cv2.destroyAllWindows()
