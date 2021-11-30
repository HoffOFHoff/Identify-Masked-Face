
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

# Show the picture with landmarks
marked_face.show()
