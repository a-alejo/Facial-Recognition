# This code extracts and separates individual faces from an image

from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./images/groups/group1.jpg')
face_locations = face_recognition.face_locations(image)

# for loop to cycle through face locations & then pulls faces from images
for face_location in face_locations:
    top, right, bottom, left = face_location
    # face image variable to get data in an array to use in the PIL library
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
    # f string to dictate in which order to save image
    pil_image.save(f'{left}.jpg')
