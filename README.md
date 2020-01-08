# WIP

Simple REST server for extracting features from images and suggesting tags.

# Install

- create `venv`
- `pip install requirements.txt`

# Activate

`$ source venv/Scripts/activate`


# Bottle server

python server.py
- runs on `gunicorn`

# Environment setup

- ENV (set to `production` to run on `gunicorn`)
- PORT (default to 3000)

# Endpoints

POST `/face-detect`
Sample reqest included in insomnia-data (for Insomnia client).


```javascript
{
  "endpoint": "face-detect",
  "success": true,
  "data": [
    {
      "box": [
        454,
        297,
        78,
        106
      ],
      "confidence": 0.9999872446060181,
      "keypoints": {
        "left_eye": [
          482,
          335
        ],
        "right_eye": [
          518,
          337
        ],
        "nose": [
          501,
          356
        ],
        "mouth_left": [
          481,
          375
        ],
        "mouth_right": [
          511,
          377
        ]
      },
      "coordinates": {
        "x": [
          454,
          532
        ],
        "y": [
          297,
          403
        ]
      }
    },
    {
      "box": [
        172,
        545,
        65,
        78
      ],
      "confidence": 0.999984860420227,
      "keypoints": {
        "left_eye": [
          184,
          573
        ],
        "right_eye": [
          214,
          578
        ],
        "nose": [
          193,
          592
        ],
        "mouth_left": [
          183,
          603
        ],
        "mouth_right": [
          209,
          607
        ]
      },
      "coordinates": {
        "x": [
          172,
          237
        ],
        "y": [
          545,
          623
        ]
      }
    },
    {
      "box": [
        817,
        555,
        58,
        70
      ],
      "confidence": 0.9999197721481323,
      "keypoints": {
        "left_eye": [
          828,
          580
        ],
        "right_eye": [
          855,
          584
        ],
        "nose": [
          836,
          594
        ],
        "mouth_left": [
          826,
          606
        ],
        "mouth_right": [
          850,
          608
        ]
      },
      "coordinates": {
        "x": [
          817,
          875
        ],
        "y": [
          555,
          625
        ]
      }
    },
    {
      "box": [
        361,
        746,
        58,
        74
      ],
      "confidence": 0.9985482096672058,
      "keypoints": {
        "left_eye": [
          373,
          772
        ],
        "right_eye": [
          401,
          775
        ],
        "nose": [
          381,
          788
        ],
        "mouth_left": [
          371,
          801
        ],
        "mouth_right": [
          396,
          804
        ]
      },
      "coordinates": {
        "x": [
          361,
          419
        ],
        "y": [
          746,
          820
        ]
      }
    }
  ]
}```


## TODO

- Cleanup the requirements (remove yolo model)
- ~~Bottle image upload (multipart)~~
- Resize uploaded image (test for performance)