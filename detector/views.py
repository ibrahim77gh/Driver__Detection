import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCssiNi_NCUDmaK2mg0VRWElUpVMkVs-pI",
  "authDomain": "driverdetection-64c39.firebaseapp.com",
  "projectId": "driverdetection-64c39",
  "storageBucket": "driverdetection-64c39.appspot.com",
  "messagingSenderId": "237746441834",
  "appId": "1:237746441834:web:654aeb7aa80ad4cb464413",
  "measurementId": "G-0JWT2VTQGV"
}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.authentication()
db=firebase.database()
store=firebase.storage()
