import matplotlib.pyplot as pyplot
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

def face_detect(image, confidence = 0.8):
    # load the image
    pixels = pyplot.imread(image)

    # detect faces in the image
    faces = detector.detect_faces(pixels)

    # extract the bounding box from the first face
    list = []
    for num, face in enumerate(faces, start = 1):
        # print(face)
        if face['confidence'] < confidence:
            print('Skipping recognized face, confidence too low')
            continue
            
        # Create coordinates    
        x1, y1, width, height = face['box']
        x2, y2 = x1 + width, y1 + height
        face['coordinates'] = { 'x': [x1, x2], 'y': [y1, y2]}
        
        # NOTE: simple writing to file
        # folder, file = url.split('/')
        # to_write = pixels[y1:y2, x1:x2]
        # pyplot.imsave('test/'+str(num)+file, to_write)
        list.append(face)
        
    # print('Found faces:', list)
    return faces

