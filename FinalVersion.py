# The merged version of the face recognition project
import os
import logging
import glob
from PIL import Image

def interface():
    print("If you want to take photos enter 'g' ")
    print("If you want to come to the Facial recognition Login enter 'l' ")
    print("If you want to exit enter 'q' ")
    test = True
    # show the user interface 

    while test:
        Instruction = input('Enter your instruction:')
        if Instruction == "g":
            print("first step")
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            
            from Mask_adding import mask_img,find_landmasks
            facelandmarks = find_landmasks()
            list_of_user = glob.glob(r"data/faces_from_camera/*/*.png")
            ori_img_dir=os.path.abspath(list_of_user[0])
            mask_img(ori_img_dir, mask_img_dir="images/surgical.png",
             facelandmarks=facelandmarks)
            
        if Instruction == "l":
            print("second step")
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            from Samility_detect import img_show
            img_show()
            from worked import show_the_user
            show_the_user()
            
            # image_show()
        if Instruction == "q":
            test = False
            print("See you!That's the end.")
            os._exit(0)
            # f = open("The face result.txt", 'a')
            # f.write('The same person')
            # f.close()


if __name__ == "__main__":
    interface()