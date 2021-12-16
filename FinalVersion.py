# -*- coding: utf-8 -*-
'''
EN.640.635 Software Carpentry
Final_Project -Identify-Masked-Face-
************ Final Version.The combined version ***********

In this project, we want to show a placid everyday scene -- you will stare at the 
webcam, and here is a line lettering: Who you are. Our project could recognize who you
are even when you wear mask! The most exciting thing is that: we do not need to use
model or machine learning method to make it.
It won't take up a lot of your computer's memory to train complex models! We only need 
the package self-contained tools in python: Face_recognition. Then we use artificial 
masked face as the new model.
Is it cool?
Now let's enjoy it!
'''
# Firstly, we need to import some useful packge for our project.
# Since we seperate our 700 around lines into four documents, some package will
# show in the other place. 
# The merged version of the face recognition project
import os
import logging
import glob
from PIL import Image
# The main body of our project
def interface():
    '''
    Combine part1.GUI, part2.Masked_adding, part3.Similarity_detect and
    part4.worked together, so it could save time and make the whole project
    more readable and visible.

    **Parameters**
        fptr: *str*
            The
        mask: *int*
            The 

    **Returns**
        One comparison.png
        One folder data/faces_from_camera
        One folder Masked_faces

    '''
    print("If you want to take photos enter 'g' ")
    print("If you want to come to the Facial recognition Login enter 'l' ")
    print("If you want to exit enter 'q' ")
    test = True
    # show the user interface 
    while test:
        Instruction = input('Enter your instruction:')
        if Instruction == "g":
            print("first step")
            print("Now please take off your mask")
            print("We recommend you inpput your name such as 'Jack' ")
            print("You should not use '_' or '/' ")
            print("///////////////////////////////")
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            print("Now you will see your artificial masked face")
            print("///////////////////////////////")       
            from Mask_adding import mask_img,find_landmasks
            facelandmarks = find_landmasks()
            list_of_user = glob.glob(r"data/faces_from_camera/*/*.png")
            ori_img_dir=os.path.abspath(list_of_user[0])
            mask_img(ori_img_dir, mask_img_dir="images/surgical.png",
             facelandmarks=facelandmarks)
            print("Now you could type l and come to second setp")
            print("///////////////////////////////") 
            
        if Instruction == "l":
            print("second step")
            print("Now you could take on your mask and take new photo")
            print("We recommend you inpput a new name such as 'JackMASKED' ")
            print("You should not use '_' or '/' ")
            print("///////////////////////////////") 
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            print("Now you could see the comporison.png show our result")
            print("///////////////////////////////") 
            from Similarity_detect import img_show
            img_show()
            print("Now you could see the video webcam interface")
            print("You could find your name is showed under your face")
            print("When you wear mask, it will show name like  JackMASKED ,")
            print("When you do not wear anthing, it will show the first name you type in")
            print("///////////////////////////////") 
            from worked import show_the_user
            show_the_user()
        # Whenever you want leave, you could type q
        if Instruction == "q":
            test = False
            print("See you!That's the end.")
            os._exit(0)
            # f = open("The face result.txt", 'a')
            # f.write('The same person')
            # f.close()


if __name__ == "__main__":
    interface()