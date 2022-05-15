import cv2
import numpy as np
import matplotlib.pyplot as plt

path = 'lena.png'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
height, width = img.shape
kernel_size = 7
sigma = (kernel_size - 1) // 6
kernel = np.zeros((kernel_size, kernel_size))
st = kernel.shape[0]//2
ed = kernel.shape[1]//2

import math
def gaussian_filter(x, y, sigma):
  PI = math.pi
  return (1/(2*PI*sigma**2))*math.exp(-(x**2+y**2)/(2*sigma**2))

for i in range(-st, st+1):
  for j in range(-ed, ed+1):
    kernel[i+st][j+ed] = gaussian_filter(i, j, sigma)

gaussian_img = np.zeros((height, width))

for row in range(st, height-st):
  for col in range(ed, width-ed):
    img_portion = img[row-st:row+st+1, col-ed:col+ed+1]
    # img_portion = img_portion[::-1, ::-1]
    gaussian_img[row][col] = np.sum(img_portion*kernel)

plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(gaussian_img, cmap='gray')
plt.show()