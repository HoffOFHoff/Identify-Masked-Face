# The merged version of the face recognition project
import os
import logging

def interface():
    print("If you want to take photos enter 'g' ")
    print("If you want to come to the Facial recognition Login enter 'l' ")
    print("If you want to exit enter 'Q' ")
    test = True
    # show the user interface 
    
    while test:
        mood_type = input('Enter your mood:')
        if mood_type == "1":
            print("first step")
            from GUI import Face_Register
            logging.basicConfig(level=logging.INFO)
            Face_Register_con = Face_Register()
            Face_Register_con.run()
            from Mask_adding import mask_img
            # mask_img()
            
        if mood_type == "2":
            print("second step")
            from Samility_detect import image_show
            from worked import show_the_user
            # show_the_user()
            
            # image_show()
        if mood_type == "q":
            test = False
            print("See you!That's the end.")
            os._exit(0)
            f = open("The face result.txt", 'a')
            f.write('The same person')
            f.close()


if __name__ == "__main__":
    interface()