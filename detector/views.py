from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials, db, storage
import datetime
import base64
from django.core.files.base import ContentFile
from PIL import Image
import tempfile
from django.db import models
from django.core.files import File


def getImageName(data):
    for key, value in data.items():
        image_name = value['img']
    return image_name

class FirebaseDataView(APIView):

    def get(self, request, format=None):
        SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
        cred = credentials.Certificate('E:\Github repos\Driver_Detection\Driver__Detection\detector\serviceAccount.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://adv-driver-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app',
            'storageBucket': 'adv-driver-monitoring-system.appspot.com',
            'credential': f'{cred}'
        })

        # Realtime Database
        ref = db.reference('new')

        # Firebase Storage
        bucket = storage.bucket()

        # order_by_child will order all the objects accoring to the current_time field, and limit_to_last will only return the first object i.e. the latest
        query = ref.order_by_child('current_time').limit_to_last(1)
        # Get data from Realtime Database
        latest_obj = query.get()

        #image_name = latest_obj[list(latest_obj.keys())[0]]['img']
        image_name = '2023-03-31 11:35:34.jpg'
        # Get image from Firebase Storage using the name of image we got from Realtime Database
        image_blob = bucket.blob(image_name)
        access_token = cred.get_access_token()

        # Save the image as a new field in latest_obj
        expiry = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        latest_obj[list(latest_obj.keys())[0]]['image_url'] = image_blob.generate_signed_url( expiration=expiry)
        return Response(latest_obj)