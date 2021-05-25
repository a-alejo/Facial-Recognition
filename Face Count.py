import face_recognition

image1 = face_recognition.load_image_file('./Images/group1.jpg')
image2 = face_recognition.load_image_file('./Images/group2.jpg')
face_location_1 = face_recognition.face_locations(image1)
face_location_2 = face_recognition.face_locations(image2)

print(
    f'There are {len(face_location_1)} people in the first image '
    f'and {len(face_location_2)} people in the second image')
