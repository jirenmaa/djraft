import pyrebase
import datetime
import mimetypes
from PIL import Image

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyAhFY77h7YfJ8TRaWoDj7TmrJnmlv6xztE",
    "authDomain": "obsidian-dfba3.firebaseapp.com",
    "databaseURL": "https://obsidian-dfba3.firebaseio.com",
    "projectId": "obsidian-dfba3",
    "storageBucket": "obsidian-dfba3.appspot.com",
    "messagingSenderId": "378438565558",
    "appId": "1:378438565558:web:e0fb25d121c31e9740b017",
    "measurementId": "G-MFWC4W6DW5",
}

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)

def firebase_image_url(img):
    global firebase

    image = Image.open(img)
    mimetype = ["JPG", "JPEG", "PNG"]
    if image.format in mimetype:
        storage = firebase.storage()

        # u_timestamp = str(str(datetime.datetime.now()).encode("utf-8").hex())
        # path_cloud = "%s----%s" % (u_timestamp, str(img))

        # storage.child(path_cloud).put(img)
        # return storage.child(str(img)).get_url()

        u_timestamp = str(str(datetime.datetime.now()).encode("utf-8").hex())
        path_cloud = "%s----%s" % (u_timestamp, str(img))

        storage.child(path_cloud).put(img)
        return storage.child(path_cloud).get_url()
    else:
        return "file should be in image format"