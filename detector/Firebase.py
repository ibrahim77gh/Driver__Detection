import firebase_admin
from firebase_admin import credentials

class Firebase:
    def __init__(self):
        self.cred = credentials.Certificate('/home/advdriver/Driver__Detection/detector/serviceAccount.json')
        # E:\Github repos\Driver_Detection\Driver__Detection\detector\serviceAccount.json
        # /home/advdriver/Driver__Detection/detector/serviceAccount.json'
        self.firebase_app = None

    def get_app(self):
        if not self.firebase_app:
            self.firebase_app = firebase_admin.initialize_app(self.cred, {
                'databaseURL': 'https://adv-driver-monitoring-system-default-rtdb.asia-southeast1.firebasedatabase.app',
                'storageBucket': 'adv-driver-monitoring-system.appspot.com',
                'credential': f'{self.cred}'
            })
        return self.firebase_app