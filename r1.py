# import pyrebase
from datetime import datetime
from datetime import timedelta
from datetime import date
from firebase_admin import db, credentials  # firestore
import firebase_admin
# firebaseConfig = {
#     'apiKey': "AIzaSyCEN-VvAPIStEx6ynB_wQMtG4uJ03JVqDk",
#     'authDomain': "vaxer-86d11.firebaseapp.com",
#     'databaseURL': "https://vaxer-86d11-default-rtdb.asia-southeast1.firebasedatabase.app/",
#     'projectId': "vaxer-86d11",
#     'storageBucket': "vaxer-86d11.appspot.com",
#     'messagingSenderId': "25635290628",
#     'appId': "1:25635290628:web:68be5861c187eea44e3f51",
#     'measurementId': "G-D1VKEFZRGL"
# }
# fb = pyrebase.initialize_app(firebaseConfig)
# db = fb.database()
c = credentials.Certificate("vaxer.json")
app = firebase_admin.initialize_app(c)
f = open('vaxer_dummy_db.csv', 'r')
x = f.readlines()
ref = db.reference(url='https://vaxer-86d11-default-rtdb.asia-southeast1.firebasedatabase.app/')
ref1 = ref.child('users')
for i in range(1, len(x)):
    x[i] = x[i].split(',')
    fno = x[i][0]
    fml = x[i][4]
    mno = x[i][3]
    mml = x[i][5]
    dob = x[i][2]
    nm = x[i][1]
    d = datetime.strptime(dob, '%m/%d/%Y')
    opv_0 = d + timedelta(days=10)
    opv_1 = d + timedelta(days=42)
    opv_2 = d + timedelta(days=70)
    opv_3 = d + timedelta(days=98)
    pen_1 = d + timedelta(days=42)
    pen_2 = d + timedelta(days=70)
    pen_3 = d + timedelta(days=98)
    # pcv_1 = str(d + datetime.timedelta(days=42))
    # pcv_2 = str(d + datetime.timedelta(days=98))
    # pcv_b = str(d + datetime.timedelta(days=280))
    rvv_1 = d + timedelta(days=42)
    rvv_2 = d + timedelta(days=70)
    rvv_3 = d + timedelta(days=98)
    ipv_1 = d + timedelta(days=42)
    ipv_2 = d + timedelta(days=98)
    mr_1 = d + timedelta(days=275)
    # je_1 = str(d + datetime.timedelta(days=280))
    vit_a1 = d + timedelta(days=290)
    dpt_1 = d + timedelta(days=500)
    mr_2 = d + timedelta(days=510)
    # je_2 = str(d + datetime.timedelta(days=515))
    opv_b = d + timedelta(days=520)
    vit_a2 = d + timedelta(days=520)
    vit_a3 = d + timedelta(days=700)
    vit_a4 = d + timedelta(days=880)
    vit_a5 = d + timedelta(days=1060)
    vit_a6 = d + timedelta(days=1240)
    vit_a7 = d + timedelta(days=1420)
    vit_a8 = d + timedelta(days=1600)
    vit_a9 = d + timedelta(days=1780)
    dpt_2 = d + timedelta(days=1850)
    data1 = {fml.replace('.', '"'): {'OPV-0': str(opv_0), 'PEN-1': str(pen_1), 'OPV-1': str(opv_1), 'RVV-1': str(rvv_1), 'IPV-1': str(ipv_1), 'PEN-2': str(pen_2),  'OPV-2': str(opv_2), 'RVV-2': str(rvv_2), 'PEN-3': str(pen_3), 'OPV-3': str(opv_3), 'RVV-3': str(rvv_3), 'IPV-2': str(ipv_2), 'MR-1': str(mr_1), 'VIT-A1': str(vit_a1), 'DPT-1': str(dpt_1), 'MR-2': str(mr_2), 'OPV-B': str(opv_b), 'VIT-A2': str(vit_a2), 'VIT-A3': str(vit_a3), 'VIT-A4': str(vit_a4), 'VIT-A5': str(vit_a5), 'VIT-A6': str(vit_a6), 'VIT-A7': str(vit_a7), 'VIT-A8': str(vit_a8), 'VIT-A9': str(vit_a9), 'DPT-2': str(dpt_2), 'dob': x[i][2], 'fno': fno, 'mno': x[i][3], 'mml': x[i][5], 'name': x[i][1]}}
    ref1.update(data1)

# r = db.child('users').get()
# for i in r.each():
#     print(i.key(), i.val())
# print(r.each())


# print(type(udata))

# jo = json.dumps(udata)
# print(udata['Anish'])
import smtplib
from email.message import EmailMessage
# from json import dumps
d1 = date.today()
# z = str(opv_0 - datetime.timedelta(days=5))
z = str(d1 + timedelta(days=5))  # db.child('users').order_by_child('OPV-0').get()
# z = str(datetime.strptime(y, '%m/%d/%Y'))
m = ref1.order_by_child('fml')
# body1 = "This is to inform you that Oral Polio Vaccine - 0 of your ward is due", db.child('users').order_by_child('OPV-0'), ". Kindly make a note."
# r = db.child('mml')
def email_alert(sub):
    msg = EmailMessage()
    body = "This is to inform you that Oral Polio Vaccine - 0 of your ward is due on "+z+". Kindly make a note."
    msg.set_content(body)
    msg['subject'] = sub
    to = m
    msg['to'] = to
    user = "vaxer.solutions@gmail.com"
    msg['from'] = user
    password = 'rnjnuaxczxnagewj'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
if ref1.order_by_child('OPV-0').equal_to(z).get():
    email_alert("Vaccine reminder")
