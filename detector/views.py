from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import firebase_admin
from firebase_admin import credentials, db

class FirebaseDataView(APIView):

    def get(self, request, format=None):
        cred = credentials.Certificate('E:\Github repos\Driver_Detection\Driver__Detection\detector\serviceAccount.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://adas-11729-default-rtdb.firebaseio.com/'
        })

        ref = db.reference('new')
        # order_by_child will order all the objects accoring to the current_time field, and limit_to_last will only return the first object i.e. the latest
        query = ref.order_by_child('current_time').limit_to_last(1)
        data = query.get()
        return Response(data)