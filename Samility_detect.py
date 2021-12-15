import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob
# from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
from skimage import transform,data
from skimage import io
from PIL import Image


img = io.imread('data/faces/img_face_1.png')
img_mask = io.imread('data/Masked_faces/img_face_3_N95.png')
img_real = io.imread('data/Masked_faces/img_face_3_surgical_blue.png')

print(img_mask.shape)
print(img.shape)
print(img_real.shape)

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
                         sharex=True, sharey=True)
ax = axes.ravel()

mse_none = mean_squared_error(img, img)
ssim_none = ssim(img, img, multichannel=True, data_range=img.max() - img.min())

mse_masked = mean_squared_error(img, img_mask)
ssim_masked = ssim(img, img_mask, multichannel=True,
                  data_range=img_mask.max() - img_mask.min())

mse_real = mean_squared_error(img, img_real)
ssim_real = ssim(img, img_real, multichannel=True,
                  data_range=img_real.max() - img_real.min())

ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[0].set_xlabel(f'MSE: {mse_none:.2f}, SSIM: {ssim_none:.2f}')
ax[0].set_title('Original image')

ax[1].imshow(img_mask, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[1].set_xlabel(f'MSE: {mse_masked:.2f}, SSIM: {ssim_masked:.2f}')
ax[1].set_title('Image with mask')

ax[2].imshow(img_real, cmap=plt.cm.gray, vmin=0, vmax=1)
ax[2].set_xlabel(f'MSE: {mse_real:.2f}, SSIM: {ssim_real:.2f}')
ax[2].set_title('Image in real life')

if ssim_real - ssim_masked < 0.1:
    print('the same person')

plt.tight_layout()
plt.show()