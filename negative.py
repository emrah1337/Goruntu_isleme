import cv2 as cv2

resim = cv2.imread("picture1.jpg")
#img_neg = cv2.imread("picture1.jpg")

#  LONG method to convert image to negative
#  This method is not for gray images
# rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
#
#  for i in range(img.shape[0]):
#      for j in range(img.shape[1]):
#         print(img[i,j])
#
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         img_neg[i,j,0] = 255 - img_neg[i, j,0] - 1
#         img_neg[i, j, 1] = 255 - img_neg[i, j,1] - 1
#         img_neg[i, j, 2] = 255 - img_neg[i, j,2] - 1
        # pixel = img_neg[i, j]
        # pixel[0] = 255 - pixel[0] - 1 # mavi
        # pixel[1] = 255 - pixel[1] - 1 # yesil
        # pixel[2] = 255 - pixel[2] - 1 # kirmizi
        # img_neg[i, j] = pixel


negative_resim = 255 - resim # (256-1) - resim

cv2.imshow("Original", resim)
#cv2.imshow("Negative_long", img_neg)
cv2.imshow("negative_short", negative_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
