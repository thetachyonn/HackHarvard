from PIL import Image
import pytesseract
import argparse
import cv2
import os
import json
import urllib2

class org_key:

    def __init__(self):
        pass
    @classmethod
    def get_response(cls, key):
        req = urllib2.Request('https://vtestapi.voatz.com/voatz/organizations/orgkey/login')
        req.add_header('Content-Type', 'application/json')
        json_data = \
            {
                "orgKey": key
            }
        response = urllib2.urlopen(req, json.dumps(json_data))
        return response
    @classmethod
    def read_response(cls, response):
        return response.info()["Csrf-Token"], response.info()["Set-Cookie"]

class register_user:

    def __init__(self):
        pass

    @classmethod
    def get_text(self, image_path):
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.threshold(gray, 0, 255,
                             cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        text = pytesseract.image_to_string(gray)
        print(text)

#response = org_key.get_response(984402)
#csrf, cookie = org_key.read_response(response)
register_user.get_text("photo_id.jpg")