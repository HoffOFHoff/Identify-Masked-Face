# Identify-Masked-Face
This is a facial identification project for the EN.540.635 “Software Carpentry”. 



# Project Topic:
It has been the third year since Covid-19's outbreak, we have all experienced a lot of incoveniences during this part of the time.
A great deal of face recognition softwares which used to work have started to face difficulties since people are now wearing masks, thus, in this project we aim to recognize people faces with masks on and compare them with the faces without masks.
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
We use python 3.6 as our language.
The basic toolboxs（such as OpenCV, dlib, face_recognition）need to be pipped in the python system.
```
pip install opencv-python
pip install opencv-contrib-python
pip install python-utils
```
We also require
dlib==19.17.0
numpy==1.21.3
scikit-image==0.18.3
pandas==1.3.4

# Support Information

## Group member: 
1. Bo Chao, bchao4@jh.edu, pkocattoss  
2. Ziying Xu, zxu92@jh.edu, HoffOFHoff

## The testing models:
The real facial model is storaged here: [Models](https://pages.github.com/)

## Important Reference for this subject
> There are some reference from some amazing groups worldwide, and we will give our superior respect to those scientists.  
> JDAI opensource based on PyTorch:  https://github.com/JDAI-CV/FaceX-Zoo.   
> Methods such as MTCNN Mobilenet and Facenet were used for face mask detection and recognition： https://github.com/mext169/detect-and-recognize-mask-face.   
> Wear the mask on people face: https://github.com/jacke121/MaskTheFace.   

# Acknowledagement 
This is an interesting class, and we learned a lot.  
**Thank for our teacher Divya Sharma.** We are eternally grateful for your patience and rigorous research attitude. 
