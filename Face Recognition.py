# This code has face recognition that identifies if a person is in another photo

import face_recognition

# Identifies Elon musk and creates an array
Elon_Musk = face_recognition.load_image_file('./images/known/Elon_Musk.jpg')
Elon_face_encoding = face_recognition.face_encodings(Elon_Musk)[0]
# Pass unknown image directory to compare
unknown_image = face_recognition.load_image_file('./images/unknown/gettyimages-SATELLITE_2020.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces to then print using Elif statement
results = face_recognition.compare_faces([Elon_face_encoding], unknown_face_encoding)

if results[0]:
    print('This is Elon Musk')
else:
    print('This is not Elon Musk')
