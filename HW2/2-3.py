import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np
# Glaucoma
img = cv.imread('jojo.jpg').astype(np.float32)/255.0  
#讀取影像

# Gaussian kernel
x, y = np.mgrid[-np.size(img,0)/2:np.size(img,0)/2, int(-np.size(img,1)/2):int(np.size(img,1)/2)]
#建立與影像同尺寸的2D高斯濾鏡
sigma = 14**2
gaussian_kernel= np.exp(-(x**2+y**2)/(sigma**2))

#Normalization
gaussian_kernel = gaussian_kernel / gaussian_kernel.max()
#將濾鏡數值矩陣的每個數值除以其最大值。
print(gaussian_kernel.shape)
blur = np.zeros(img.shape)
fig = plt.figure()


blur[:,:,0] = (img[:,:,0] * gaussian_kernel)
blur[:,:,1] = (img[:,:,1] * gaussian_kernel)
blur[:,:,2] = (img[:,:,2] * gaussian_kernel)
#再將濾鏡點對點乘上影像的 RGB 值
blur = (blur*255).astype(np.uint8)
#儲存影像
if not os.path.exists('images'):
    os.mkdir('images')
cv.imwrite('test2-3.jpg', blur)