# Todo Bottle REST API
from bottle import route, run, Response, request
from time import perf_counter 
import os
from src.face_detect import face_detect


# ENV Variables
IS_PRODUCTION = os.environ.get('ENV', None) == 'production'
PORT = os.environ.get('PORT', 8080)
FACE_DETECT_CONFIDENCE = os.environ.get('FACE_DETECT_CONFIDENCE', 0.8)





# ROUTES
@route('/face-detect', method='post')
def index():
    upload = request.files.get('image')
    name, ext = os.path.splitext(upload.filename)
    print('File extension', upload)
    if ext.lower() not in ('.jpg', '.jpeg'):
        Response.status = 400 # set to BadRequest
        return { 'success': False, 'message': "Only .jpg and .jpeg fiels are allowed."}
    
    
    print('image uploaded')
    t1_start = perf_counter()  
    result = face_detect(upload.file, confidence=FACE_DETECT_CONFIDENCE)
    t1_stop = perf_counter() 
    print('face detection took (seconds):', t1_stop - t1_start)
    return {'endpoint': '/face-detect', 'success': True, 'data': result}


# Production server
if IS_PRODUCTION:
    print('Running in production mode')
    run(server='gunicorn', host = 'localhost', port = PORT)
else:
    print('Running in development mode')
    run(host='localhost', port=PORT)
