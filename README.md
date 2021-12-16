# Identify-Masked-Face
This is a facial identification project for the EN.540.635 “Software Carpentry”. 



# Project Topic:
It has been the third year since Covid-19's outbreak, we have all experienced a lot of inconveniences during this part of the time.  
A great deal of face recognition software which used to work have started to face difficulties since people are now wearing masks, thus, in this project we aim to recognize people faces with masks on and compare them with the faces without masks.  
The three milestones we needed to overcome in the project.  
1. Face identification.  
2. Mask the face.  
3. Identify and compare the masked face with the unmasked face.  
4. Identify real masked face using webcam



#### The procedure of 1.Face identification:
Show the GUI for users to take photos while they wear mask or they do not wear mask.  
1.We used a package within python/face_recognition to deal with the problem.

#### The procedure of 2.Mask the face:
We will add mask on every face we have already capture in the part1.GUI.  
1. Obtain raw mask pictures with photoshop  
2. Use the recognized face and its landmarks in step one  
3. Put the mask on to the face by attaching them to proper landmarks  


#### The procedure of 3.Identify and compare the masked face with the unmasked face.  
In this project, we want to write one function that can compare the 
similarity between our artificial masked artificial face with the masked face
in our life. Then we will show the SSIM parameter as the indicator of evaluation.
The img_show() function will be used in the mainbody--FinalVersion.py and the picture
will be saved in our Identify-Masked-Face project. 
You could see that the faked masked face is close to the real masked face, and
is closer in difference.
1.

#### The procedure of 4. Identify real masked face using webcam
In this project, we want to show a placid everyday scene -- you will stare at the 
webcam, and here is a line lettering: Who you are.  
Our project could recognize who you are even when you wear mask! The most exciting thing is that: we do not need to use model or machine learning method to make it.  
It won't take up a lot of your computer's memory to train complex models! We only need the package self-contained tools in python: Face_recognition.  
Then we use artificial masked face as the new model.  
Is it cool?  
Now let's enjoy it!  
1.

# Project Arrangement

## TimeTable
11.30-12.5 Previous work reading, brain storming, face recognition and obtaining landmarks  
12.4-12.7 Adding mask to faces and start face comparing  
12.8-12.13 Making GUI and completing face comparing  
12.13-12.15 Wrap up and writing README  
12.16 Unit test, PEP8 test and Release  


## Environment Organization
**We use python 3.8.8 as our language.**  
The basic toolboxes（such as OpenCV, dlib, face_recognition）need to be pipped in the python system.    
**We also require**  
dlib==19.17.0  
OpenCV==4.5.4  
numpy==1.21.3  
scikit-image==0.18.3  
face_recognition==1.2.3  
The machine leaning model is sel-contained in the face_recognition package.

## How to use the code
**Notice: Whenever you want leave, you could type q!**  
1. Open the FinalVersion.py  
2. Click and Run code  
3. Follow the instruction on the command  
4. Now please take off your mask and type g and ready to GO! You will take photo.  
5. Now you will see your artificial masked face, which is added by our code.  
6. Now you could type l and come to second setp  
7. Now you could take on your mask and take new photo  
8. Now you could see the comporison.png show our result
9. Now you could see the video webcam interface. You could find your name is showed under your face. When you wear mask, it will show name like 'JackMASKED'. When you do not wear anthing, it will show the first name you type in.

> You might not use _ or / in your input name, which might make difficult in our path recognition.  


# Support Information

## Group member: 
1. Bo Chao, bchao4@jh.edu, pkocattoss  
2. Ziying Xu, zxu92@jh.edu, HoffOFHoff

## The testing models:
The real facial model is stored here: [Models](https://pages.github.com/)

## Important Reference for this subject
> The inspiring ideas from amazing groups worldwide helped us through this this project, we would like to give them our superior respect.  
> JDAI opensource based on PyTorch:  https://github.com/JDAI-CV/FaceX-Zoo.     
> Methods such as MTCNN Mobilenet and Facenet were used for face mask detection and recognition: https://github.com/mext169/detect-and-recognize-mask-face.  
> Face recognition using the camera: https://github.com/coneypo/Dlib_face_recognition_from_camera  
> Wear the mask on people face: https://github.com/jacke121/MaskTheFace.  
> Face recognition official website: https://towardsdatascience.com/building-a-face-recognizer-in-python-7fd6630c6340  
> Scikit offcial website: https://scikit-image.org/  

# Acknowledgement 
**Special thanks towards our teacher Divya Sharma.**  
We are very grateful for your patience and rigorous research attitude.  
