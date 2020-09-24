import os
import pathlib
import pyrebase
import datetime
import mimetypes

from PIL import Image
from django.core.files.storage import FileSystemStorage

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

def firebase_image_url(file, obj):
    global firebase

    image = Image.open(obj)
    file_storage = FileSystemStorage()
    mimetype = ["JPG", "JPEG", "PNG"]

    if image.format in mimetype:
        storage = firebase.storage()

        # create temp file
        file_storage.save(file.name, file)

        u_timestamp = str(str(datetime.datetime.now()).encode("utf-8").hex())[:32]
        path_cloud = "cover/%s----%s" % (u_timestamp, str(file))

        # upload file to firebase
        storage.child(path_cloud).put(file)

        # delete temp file
        os.remove("%s\\media\\%s" % (
            str(pathlib.Path(__file__).parent.parent),
            file.name)
        )

        return storage.child(path_cloud).get_url()
    else:
        return "file should be in image format"