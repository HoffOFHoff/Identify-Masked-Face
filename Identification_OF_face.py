import face_recognition
from PIL import Image, ImageDraw

# Load the jpg file and use face_recognition to get the numpy type
image = face_recognition.load_image_file("test.jpeg")

# Find facial features with landmarks function
face_landmarks_list = face_recognition.face_landmarks(image)

# Use PIL imagedraw object to mark points on the face
marked_face = Image.fromarray(image)
signal = ImageDraw.Draw(marked_face)


# Show the location of each facial feature in this image
for face_landmarks in face_landmarks_list:
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(
            facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        signal.point(face_landmarks[facial_feature])

facelandmarks = []
for key in face_landmarks:
    facelandmarks.append(face_landmarks[key])
# Show the picture with landmarks
marked_face.show()


def mask_img(ori_img_dir, mask_img_dir, facelandmarks):
    """
    :param ori_img_dir: Contains the path of the person's photo
    :param mask_img_dir: Contains the path of a mask photo
    :param facelandmarks: The 72 key points on a human face
    :return: A photo with the person wearing a mask
    """

    # We load in the mask and the person's photo
    ori_img_dir = "test3.png"
    mask_img_dir = "surgical.png"
    face_pic = Image.open(ori_img_dir)
    mask_pic = Image.open(mask_img_dir)

    # Obtaining the key points of chin and nose to put on a mask
    nose_point = facelandmarks[3][1]
    nose_vector = np.array(nose_point)
    chin_left_point = facelandmarks[0][1]
    chin_right_point = facelandmarks[0][15]
    chin_bottom_point = facelandmarks[0][8]
    chin_bottom_vector = np.array(chin_bottom_point)