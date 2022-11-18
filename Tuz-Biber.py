import random
import cv2
import matplotlib.pyplot as plt

gercek_goruntu = cv2.imread("picture1.jpg", cv2.IMREAD_GRAYSCALE)
gurultulu = cv2.imread("picture1.jpg", cv2.IMREAD_GRAYSCALE)


height, width = gurultulu.shape
# number of pixels that will change
number_of_pixels_to_change = random.randint(500,10000)
for i in range(number_of_pixels_to_change):
    h = random.randint(0,height-1)
    w = random.randint(0,width-1)
    gurultulu[h,w] = 255  # add white color at random index
for i in range(number_of_pixels_to_change):
    h = random.randint(0,height-1)
    w = random.randint(0,width-1)
    gurultulu[h,w] = 0  # add black color at random index

# calculate the histogram
# calcHist(gray image , channel(for colors), mask , histSize , ranges)
histForRealImage = cv2.calcHist(gercek_goruntu, [0], None, [256], [0, 256])
histForNoiseImage = cv2.calcHist(gurultulu, [0], None, [256], [0, 256])

# plot the image and histogram
fig = plt.figure()

fig.add_subplot(221)
plt.title(' Gerçek Görüntü ')
plt.set_cmap('gray')
plt.imshow(gercek_goruntu)

fig.add_subplot(222)
plt.title('histogram ')
plt.plot(histForRealImage)

fig.add_subplot(223)
plt.title(' Gürültülü Görüntü ')
plt.set_cmap('gray')
plt.imshow(gurultulu)

fig.add_subplot(224)
plt.title('histogram ')
plt.plot(histForNoiseImage)

fig.tight_layout()
plt.show()
