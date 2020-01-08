# cleverimage

**THIS PROJECT IS STILL WIP!!!**

Simple REST server for extracting features from images and suggesting tags.

## Install

- create `venv`
- `pip install requirements.txt`
- `$ source venv/Scripts/activate`
- `py server.js` (runs bottle server)


## Environment variables

Environment configuration:

| Variable | Description | Required  | Default value |
| ----| --- | ---| --- |
| `ENV` | If set to `production` server will run on `gunicorn` | no | N/A |
| `PORT` | Set up the server port | no | 3000 |
| `FACE_DETECT_CONFIDENCE` | Set up the confidence threshold for `face_detect`  | no | 0.8 |

# API 

Sample reqests are included in `insomnia-data.json` (for [Insomnia client](https://insomnia.rest/)).

### `POST` `/face-detect`

Detects faces in uploaded image.

```javascript
{
  "endpoint": "/face-detect",
  "success": true,
  "data": [
    {
      "box": [ 3033, 1167, 431, 575 ],
      "confidence": 0.9996196031570435,
      "keypoints": {
        "left_eye": [ 3089, 1369 ],
        "right_eye": [ 3283, 1361 ],
        "nose": [ 3135, 1514 ],
        "mouth_left": [ 3124, 1612 ],
        "mouth_right": [ 3275, 1610 ]
      },
      "coordinates": {
        "x": [ 3033, 3464 ],
        "y": [ 1167, 1742 ]
      }
    }
  ]
}
```


## TODO

- Cleanup the requirements (remove yolo model)
- ~~Bottle image upload (multipart)~~
- Resize uploaded image (test for performance)