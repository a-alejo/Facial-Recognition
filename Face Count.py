
import face_recognition

image = face_recognition.load_image_file('./Images/group1.jpg')
face_locations = face_recognition.face_locations(image)

print(f'There are {len(face_locations)} people in this image')