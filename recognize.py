import matplotlib.pyplot as pyplot
from mtcnn.mtcnn import MTCNN
from PIL import Image
from numpy import asarray

detector = MTCNN()


def face_detect(url):
    # load the image
    pixels = pyplot.imread(url)
    # detect faces in the image
    faces = detector.detect_faces(pixels)

    # extract the bounding box from the first face
    list = []
    for face in faces:
        print(face)
        if face['confidence'] < 0.9:
            print('Skipping recognized face, confidence too low')
            continue
        x1, y1, width, height = face['box']
        x2, y2 = x1 + width, y1 + height
        face['coordinates'] = { 'x': [x1, x2], 'y': [y1, y2]}
        list.append(face)
    print('Found faces:', list)
    return list

face_detect("samples/1.jpg")