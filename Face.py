import face_recognition
from PIL import Image, ImageDraw



a = face_recognition.load_image_file('bill.jpg')
bill_face_encoding = face_recognition.face_encodings(a)[0]

b = face_recognition.load_image_file('mark.jpg')
mark_face_encoding = face_recognition.face_encodings(b)[0]

known_face_encodings = [
    bill_face_encoding,
    mark_face_encoding
]


known_face_names = [
     'Bill Gates',
     'Mark Zuckerberg'
]


test_image = face_recognition.load_image_file('vv.jpg')

face_locations = face_recognition.face_locations(test_image)
print(face_locations)
print(f'There are {len(face_locations)} people in this image')

face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)

draw = ImageDraw.Draw(pil_image)

for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
    name = ('unknown Person')
    if True in matches:
        first_match_index =matches.index(True)
        name = known_face_names[first_match_index]

    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))



    text_width, text_height = draw.textsize(name)

    draw.rectangle(((left, bottom - text_height -10), (right, bottom)), fill=(0,0,0),
    outline=(0,0,0))



    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

pil_image.show()
pil_image.save('identify.jpg')










    
    
