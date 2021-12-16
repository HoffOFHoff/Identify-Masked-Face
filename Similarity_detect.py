# -*- coding: utf-8 -*-
'''
EN.640.635 Software Carpentry
Final_Project -The Similarity_detect

Part 3.Similarity comparison 

In this project, we want to write one function that can compare the 
similarity between our virtual masked face and the face wearitng a mask
in our life. Then we calculate the SSIM parameter, it works as the indicator of evaluation.
The img_show() function will be used in the mainbody--Interface.py and the picture
will be saved in our Identify-Masked-Face project. 
You could see that the virtual masked face is similar with the real masked face.
1. We generate the interface of the img_show comparison.
2. Use skimage to detect the MSE and SSIM parameter to check the difference
3. The comparison will show if it think that those virtual mask are the 
same with the real masked face in daily life.
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error
from skimage import transform,data
from skimage import io
from PIL import Image

def img_show():
    '''
    Apply skimage to determine the similarity of the line structure of an image. 
    It needs both the original image and your newly-masked image and . 
    There will be a figure showen to compare your face with
    our model. In the meanwhile, there will be one figure showing the detailed 
    comparison which saved in-situ.

    **Parameters**

        list_of_user: *list*
            All the people once taked photo with our project.
            (ex.['/Users/xuziying/Desktop/data/faces_from_camera/person_1
            _chaobo/img_face_1.png','/Users/xuziying/Desktop/data/faces_
            from_camera/person_2_ziying/img_face_1.png'])

        img_path: *str*
            This varible store the absolute path of our photo from webcam. 
            (ex. /Users/xuziying/Desktop/data/faces_from_camera/person_1_chaobo).
        
        img_mask_path: *str*
            This varible store the absolute path of the photo which we add an 
            virtual mask on it. 
            (ex. /Users/xuziying/Desktop/data/Masked_faces/person_1_chaobo_surgical.png).        
        
        ssim_masked: *turple*
            The complex model to determine the similarity between the virtual masked
            picture and the real face without mask.

        ssim_real: *turple*
            The complex model to determine the similarity between the real face with
            mask and the virtual face with mask.

    **Returns**

        None
        

    For extra info:

        *https://scikit-image.org/
    '''

    # We use three images seperately, and compare those figures.
    # Here we convert to RGB to circumvent some issues with different
    # file formats.
    list_of_user = glob.glob(r"data/faces_from_camera/*/*.png")
    img_path = list_of_user[0]
    img_real_path = list_of_user[1]
    print(img_path)
    print(img_real_path)
    list_of_artificial_user = glob.glob(r"data/Masked_faces/*.png")
    img_mask_path = list_of_artificial_user[0]
    print(img_mask_path)

    # Usually, when we add mask to our face, the size of the picture will
    # change, so we use the transform.resize function to make they casually
    # similar. Otherwise the comparison will fail.
    img = io.imread(img_path)
    (x,y,z)=img.shape
    img_mask = io.imread(img_mask_path)
    img_mask = transform.resize(img_mask,(x,y,z))
    img_real = io.imread(img_real_path)
    img_real = transform.resize(img_real,(x,y,z))

    # Generate the interface of the img_show comparison.
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4),
                            sharex=True, sharey=True)
    ax = axes.ravel()

    mse_none = mean_squared_error(img, img)
    ssim_none = ssim(img, img, multichannel=True, data_range=img.max() - img.min())

    mse_masked = mean_squared_error(img, img_mask)
    ssim_masked = ssim(img, img_mask, multichannel=True,
                    data_range=img_mask.max() - img_mask.min())

    mse_real = mean_squared_error(img, img_real)
    ssim_real = ssim(img_mask, img_real, multichannel=True,
                    data_range=img_real.max() - img_real.min())

    # Use the model of MSE and SSIM to compare the similarity.
    # SSIM means structural similarity index measure.
    # MSE means Mean Squared Error.
    # When SSIM([0,1]) is close to 0, the two fig are similar and vice versa.
    # WHen MSE is close to 0, the two fig are similar and vice versa.
    ax[0].imshow(img, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[0].set_xlabel(f'MSE: {mse_none:.2f}, SSIM: {ssim_none:.2f}')
    ax[0].set_title('Original image')

    ax[1].imshow(img_mask, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[1].set_xlabel(f'MSE: {mse_masked:.2f}, SSIM: {ssim_masked:.2f}')
    ax[1].set_title('Image with mask')

    ax[2].imshow(img_real, cmap=plt.cm.gray, vmin=0, vmax=1)
    ax[2].set_xlabel(f'MSE: {mse_real:.2f}, SSIM: {ssim_real:.2f}')
    ax[2].set_title('Image in real life')

    # The comparison will show 
    if  ssim_real > 0.5:
        print('the same person')
    else:
        print('a bit different')


    plt.tight_layout()
    plt.savefig('comparison.png',bbox_inches='tight')
    plt.show()

img_show()