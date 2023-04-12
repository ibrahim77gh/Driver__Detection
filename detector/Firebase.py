import firebase_admin
from firebase_admin import credentials

class Firebase:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_firebase()
        return cls._instance

    def _initialize_firebase(self):
        # /home/advdriver/Driver__Detection/detector/serviceAccount.json'
        # E:\Github repos\Driver_Detection\Driver__Detection\detector\serviceAccount.json
        self.cred = credentials.Certificate('/home/advdriver/Driver__Detection/detector/serviceAccount.json')
        self.firebase_app = firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://adv-driver-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app',
            'storageBucket': 'adv-driver-monitoring-system.appspot.com',
            'credential': f'{self.cred}'
        })

    def get_app(self):
        return self.firebase_app