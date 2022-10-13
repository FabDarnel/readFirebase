# This script aims at streaming ESP32 IoT data from Firebase to a webapp 
"""
****************Read Firebase Realtime Database**************
"""

"""
sources:
 https://codeloop.org/python-firebase-real-time-database/
 firebase console--> project overview--> project settings -->service accounts --> python
 https://www.codespeedy.com/reading-data-from-firebase-database-using-python-script/
 https://www.youtube.com/watch?v=mNMv3WNgp0c
 https://www.youtube.com/watch?v=DCaH4bQ4DxA

"""
# import firebase - backend as a service, Backend-as-a-Service (BaaS)
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate("********")  # Paste the path to the serviceAccount.json file

# Initialise the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': '********/'  # paste the databaseURL obtained from Firebase Console
    })

# Assign the Firebase database to a reference variable 
ref = db.reference('********/') # Paste the database parent directory name

def readFirebase(ref):
    # Read Firebase database 
    dbValue = db.reference('********')

    # print(ref.get())  // used for debugging 
    return ref.get()