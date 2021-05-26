# This code matches faces and identifies defined person name with a blue box with and displays unmatched
# persons as unknown

import face_recognition
from PIL import Image, ImageDraw

# Identifies Elon musk and creates an array
Elon_Musk = face_recognition.load_image_file('./images/known/Elon_Musk.jpg')
Elon_face_encoding = face_recognition.face_encodings(Elon_Musk)[0]
# Same as above but now for Bill Gates
Bill_Gates = face_recognition.load_image_file('./images/known/Bill_Gates.jpg')
Bill_face_encoding = face_recognition.face_encodings(Bill_Gates)[0]

# Create an array of encodings and names
known_face_encodings = [Elon_face_encoding, Bill_face_encoding]
known_face_names = ['Elon Musk', 'Bill Gates']

# Importing an image
test_image = face_recognition.load_image_file('./images/unknown/economictimes.indiatimes.jpg')
# Testing finding faces in image above
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Formatted to use the PIL library
pil_image = Image.fromarray(test_image)

# An instance of ImageDraw to crete box around image
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
    name = 'Unkown Person'

    # if statement to match
    if True in matches:
        first_match_index = matches.index(True)
        # Selects first name of known faces to match
        name = known_face_names[first_match_index]

    # Draw box around face
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Add labels
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255))

# As per PIL doc it's recommended to delete the draw instance
del draw
pil_image.show()

# PIL library to save image with identified box
pil_image.save('identified.jpg')
