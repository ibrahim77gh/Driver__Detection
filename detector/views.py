from django.shortcuts import render
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCssiNi_NCUDmaK2mg0VRWElUpVMkVs-pI",
  "authDomain": "driverdetection-64c39.firebaseapp.com",
  "databaseURL":"https://driverdetection-64c39-default-rtdb.firebaseio.com/"
  "projectId": "driverdetection-64c39",
  "storageBucket": "driverdetection-64c39.appspot.com",
  "messagingSenderId": "237746441834",
  "appId": "1:237746441834:web:654aeb7aa80ad4cb464413",
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()
database=firebase.database()
storage=firebase.storage()


def home(request):
    Name=database.child('Data').child('Name').get().val()
    Copartner=database.child('Data').child('Copartner').get().val()
    Project=database.child('Data').child('Project').get().val()

    return render(request,'home.html',{
        "Name":Name,
        "Copartner":Copartner,
        "Project":Project
    })




