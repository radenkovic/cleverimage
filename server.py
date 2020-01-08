# Todo Bottle REST API
from bottle import route, run
import os
from src.face_detect import face_detect



@route('/face-detect')
def index():
    # TODO load image multipart and switch to POST
    result = face_detect('samples/4.jpg')
    # TODO format response
    return {'endpoint': 'face-detect', 'success': True, 'data': result}


# ENV Variables
IS_PRODUCTION = os.environ.get('ENV', None) == 'production'
PORT = os.environ.get('PORT', 8080)

# Production server
if IS_PRODUCTION:
    print('Running in production mode')
    run(server='gunicorn', host = 'localhost', port = PORT)
else:
    print('Running in development mode')
    run(host='localhost', port=PORT)
