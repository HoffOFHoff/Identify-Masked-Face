# Identify-Masked-Face
This is a facial identification project for the EN.540.635 “Software Carpentry”. 



# Project Topic:
It has been the third year since Covid-19's outbreak, we have all experienced a lot of inconveniences during this part of the time.
A great deal of face recognition software which used to work have started to face difficulties since people are now wearing masks, thus, in this project we aim to recognize people faces with masks on and compare them with the faces without masks.
The three milestones we needed to overcome in the project.  
1.Face identification.  
2.Mask the face.  
3.Identify and compare the masked face with the unmasked face.  



#### The procedure of 1.Face identification:
1.We used a package within python/face_recognition to deal with the problem.

#### The procedure of 2.Mask the face:
1.Obtain raw mask pictures with photoshop
2.Use the recognized face and its landmarks in step one
3.Put the mask on to the face by attaching them to proper landmarks


#### The procedure of 3.Identify and compare the masked face with the unmasked face.  
1.

# Project Arrangement

## TimeTable
![image](https://user-images.githubusercontent.com/)


## Environment Organization
We use python 3.8.8 as our language.
The basic toolboxes（such as OpenCV, dlib, face_recognition）need to be pipped in the python system.
We also require
dlib==19.17.0
OpenCV==4.5.4
numpy==1.21.3
scikit-image==0.18.3
face_recognition==1.2.3

## How to use the code

# Support Information

## Group member: 
1. Bo Chao, bchao4@jh.edu, pkocattoss  
2. Ziying Xu, zxu92@jh.edu, HoffOFHoff

## The testing models:
The real facial model is stored here: [Models](https://pages.github.com/)

## Important Reference for this subject
> The inspiring ideas from amazing groups worldwide helped us through this this project, we would like to give them our superior respect.
> JDAI opensource based on PyTorch:  https://github.com/JDAI-CV/FaceX-Zoo.   
> Methods such as MTCNN Mobilenet and Facenet were used for face mask detection and recognition： https://github.com/mext169/detect-and-recognize-mask-face.
> Face recognition using the camera https://github.com/coneypo/Dlib_face_recognition_from_camera
> Wear the mask on people face: https://github.com/jacke121/MaskTheFace.
> Face recognition https://towardsdatascience.com/building-a-face-recognizer-in-python-7fd6630c6340
> https://scikit-image.org/

# Acknowledgement 
**Special thanks towards our teacher Divya Sharma.** We are very grateful for your patience and rigorous research attitude. 
