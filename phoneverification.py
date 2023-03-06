import pyrebase
import streamlit as st
import fb1

c = {
  'apiKey': "AIzaSyDUS6IjAVWj_CnvTHXxjMqSzMSvPEcQjl4",
  'authDomain': "vaxer-6c2d6.firebaseapp.com",
  'databaseURL': "https://vaxer-6c2d6-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "vaxer-6c2d6",
  'storageBucket': "vaxer-6c2d6.appspot.com",
  'messagingSenderId': "73347672678",
  'appId': "1:73347672678:web:a63c65f59555423f39dba7",
  'measurementId': "G-RQPH5KJJ40"
}

fb = pyrebase.initialize_app(c)
auth = fb.auth()
st.write("VAXER")
ph = st.text_input('phone number')
pw = st.text_input('password')
b = st.button('Verify')
if b:
  if ph == fb1.fno or fb1.mno:
    user = auth.send_password_reset_email(fb1.fml, pw)
    auth.send_email_verification(user['idToken'])
    st.write("Logged in successfully")
