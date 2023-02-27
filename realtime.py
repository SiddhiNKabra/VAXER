# import firebase_admin
# from firebase_admin import credentials, db
# import pyrebase
# fb = credentials.Certificate("vaxer.json")
# y = firebase_admin.initialize_app(fb)
# f = open('vaxer_dummy_db.csv', 'r')
# x = f.readlines()
# ref = db.reference(url='https://authentication-9b632-default-rtdb.asia-southeast1.firebasedatabase.app/')
# ref1 = ref.child('user')
#
# for i in range(1, len(x)):
#     x[i] = x[i].split(',')
#     fno = x[i][0]
#     fml = x[i][4]
#     mno = x[i][3]
#     mml = x[i][5]
#     data1 = {fno: {'vacdate': x[i][7], 'dob': x[i][2], 'fml': x[i][4], 'mno': x[i][3], 'mml': x[i][5],
#                    'vactype': x[i][6], 'name': x[i][1]}}
#     ref1.update(data1)


import pyrebase
# import streamlit as st

firebaseConfig = {
  'apiKey': "AIzaSyCKQ2jvuCsO3j8f0Fg5cPjB3dGqDYNr-Gg",
  'authDomain': "authentication-9b632.firebaseapp.com",
  'databaseURL': "https://authentication-9b632-default-rtdb.asia-southeast1.firebasedatabase.app/",
  'projectId': "authentication-9b632",
  'storageBucket': "authentication-9b632.appspot.com",
  'messagingSenderId': "737157709410",
  'appId': "1:737157709410:web:ee48ad960e88db766f1b3b",
  'measurementId': "G-KYF85J7086"
}
fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()
auth = fb.auth()


f = open('vaxer_dummy_db.csv', 'r')
x = f.readlines()
for i in range(1, len(x)):
    x[i] = x[i].split(',')
    fno = x[i][0]
    fml = x[i][4]
    mno = x[i][3]
    mml = x[i][5]
    data1 = {fno: {'vacdate': x[i][7], 'dob': x[i][2], 'fml': x[i][4], 'mno': x[i][3], 'mml': x[i][5],
                   'vactype': x[i][6], 'name': x[i][1]}}
    db.child('user').update(data1)

fno = x[i][0]
fml = x[i][4]
# st.write("VAXER")
# p = st.text_input("Enter registered phone number")
# pw = st.text_input("Enter password")
# b = st.button("Create and Verify")
# if b:
#     if p == fno:
#         parent = auth.create_user_with_email_and_password(fml, pw)
#         auth.send_email_verification(parent['idToken'])
#         st.write("Account created Successfully")
