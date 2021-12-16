# -*- coding: utf-8 -*-
'''
EN.640.635 Software Carpentry
Final_Project -Identify-Masked-Face-
************ Final Version.The combined version ***********

In this project, we want to show a placid everyday scene -- you will stare at the 
webcam, and it doesn't recognize you because you are wearing a mask. Our project could recognize who you
are even when you wear mask!
It won't take up a lot of your computer's memory to train complex models! We only need 
the packages which are self-contained tools in python: Face_recognition. Then we use artificial 
masked faces as the new model.
Isn't that cool?
Now let's enjoy it!
'''
# Firstly, we need to import some useful packges for our project.
# Our project contains five parts. The Interface as the main document to run the programe,
# GUI takes all photos and store them, Mask_adding puts on virtual masks for recorded faces,
# Similarity_detect compares the images to present its similarity, worked identifies your face with the camera. 
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
    print("1. Please take a photo of your self, enter 'g' ")
    print("2. Appluy facial recognition, enter 'l' ")
    print("If you want to exit, enter 'q' ")
    test = True
    # show the user interface 
    while test:
        Instruction = input('Enter your instruction:')
        if Instruction == "g":
            print("Step 1")
            print("Now please take off your mask")
            print("We recommend you input your name in the format of 'Jack' ")
            print("Please avoid using '_' or '/' ")
            print("///////////////////////////////")
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            print("Now you will see your face with an artificial mask")
            print("///////////////////////////////")       
            from Mask_adding import mask_img,find_landmasks
            facelandmarks = find_landmasks()
            list_of_user = glob.glob(r"data/faces_from_camera/*/*.png")
            ori_img_dir=os.path.abspath(list_of_user[0])
            mask_img(ori_img_dir, mask_img_dir="images/surgical.png",
             facelandmarks=facelandmarks)
            print("Please type l to perfrom step 2")
            print("///////////////////////////////") 
            
        if Instruction == "l":
            print("Step 2")
            print("Do not press the clear botton in the GUI!!!!")
            print("Please put on your mask and take a new photo")
            print("We recommend you input a new name in the format of 'JackMASKED' ")
            print("Please avoid using '_' or '/' ")
            print("///////////////////////////////") 
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            print("Now you can see the comporison.png showing the comparison result")
            print("///////////////////////////////") 
            from Similarity_detect import img_show
            img_show()
            print("Now you can see the video webcam interface")
            print("You can find your name showen under the red boxs")
            print("When you wear a mask, the user name you input while wearing a mask will be presented,")
            print("When you present your face without a mask, it will show the first name you typed in")
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