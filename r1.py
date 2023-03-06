import pyrebase
import datetime
firebaseConfig = {
    'apiKey': "AIzaSyCEN-VvAPIStEx6ynB_wQMtG4uJ03JVqDk",
    'authDomain': "vaxer-86d11.firebaseapp.com",
    'databaseURL': "https://vaxer-86d11-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "vaxer-86d11",
    'storageBucket': "vaxer-86d11.appspot.com",
    'messagingSenderId': "25635290628",
    'appId': "1:25635290628:web:68be5861c187eea44e3f51",
    'measurementId': "G-D1VKEFZRGL"
}
fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()
f = open('vaxer_dummy_db.csv', 'r')
x = f.readlines()

for i in range(1, len(x)):
    x[i] = x[i].split(',')
    fno = x[i][0]
    fml = x[i][4]
    mno = x[i][3]
    mml = x[i][5]
    dob = x[i][2]
    nm = x[i][1]
    d = datetime.datetime.strptime(dob, '%Y-%m-%d')
    opv_0 = d + datetime.timedelta(days=10)
    opv_1 = str(d + datetime.timedelta(days=42))
    opv_2 = str(d + datetime.timedelta(days=70))
    opv_3 = str(d + datetime.timedelta(days=98))
    pen_1 = str(d + datetime.timedelta(days=42))
    pen_2 = str(d + datetime.timedelta(days=70))
    pen_3 = str(d + datetime.timedelta(days=98))
    # pcv_1 = str(d + datetime.timedelta(days=42))
    # pcv_2 = str(d + datetime.timedelta(days=98))
    # pcv_b = str(d + datetime.timedelta(days=280))
    rvv_1 = str(d + datetime.timedelta(days=42))
    rvv_2 = str(d + datetime.timedelta(days=70))
    rvv_3 = str(d + datetime.timedelta(days=98))
    ipv_1 = str(d + datetime.timedelta(days=42))
    ipv_2 = str(d + datetime.timedelta(days=98))
    mr_1 = str(d + datetime.timedelta(days=275))
    # je_1 = str(d + datetime.timedelta(days=280))
    vit_a1 = str(d + datetime.timedelta(days=290))
    dpt_1 = str(d + datetime.timedelta(days=500))
    mr_2 = str(d + datetime.timedelta(days=510))
    # je_2 = str(d + datetime.timedelta(days=515))
    opv_b = str(d + datetime.timedelta(days=520))
    vit_a2 = str(d + datetime.timedelta(days=520))
    vit_a3 = str(d + datetime.timedelta(days=700))
    vit_a4 = str(d + datetime.timedelta(days=880))
    vit_a5 = str(d + datetime.timedelta(days=1060))
    vit_a6 = str(d + datetime.timedelta(days=1240))
    vit_a7 = str(d + datetime.timedelta(days=1420))
    vit_a8 = str(d + datetime.timedelta(days=1600))
    vit_a9 = str(d + datetime.timedelta(days=1780))
    dpt_2 = str(d + datetime.timedelta(days=1850))
    data1 = {fno: {'vaccination': {'OPV-0': str(opv_0), 'PEN-1': pen_1, 'OPV-1': opv_1, 'RVV-1': rvv_1, 'IPV-1': ipv_1, 'PEN-2': pen_2,  'OPV-2': opv_2, 'RVV-2': rvv_2, 'PEN-3': pen_3, 'OPV-3': opv_3, 'RVV-3': rvv_3, 'IPV-2': ipv_2, 'MR-1': mr_1, 'VIT-A1': vit_a1, 'DPT-1': dpt_1, 'MR-2': mr_2, 'OPV-B': opv_b, 'VIT-A2': vit_a2, 'VIT-A3': vit_a3, 'VIT-A4': vit_a4, 'VIT-A5': vit_a5, 'VIT-A6': vit_a6, 'VIT-A7': vit_a7, 'VIT-A8': vit_a8, 'VIT-A9': vit_a9, 'DPT-2': dpt_2}, 'dob': x[i][2], 'fml': x[i][4], 'mno': x[i][3], 'mml': x[i][5], 'name': x[i][1]}}
    db.child('users').update(data1)
import smtplib
from email.message import EmailMessage
d1 = datetime.date.today()
def email_alert(sub, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
    msg['to'] = to

    user = "vaxer.solutions@gmail.com"
    msg['from'] = user
    password = 'rnjnuaxczxnagewj'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()
if d1 == opv_0 - datetime.timedelta(days=5):
    email_alert("Vaccine reminder", "This is to inform you that Oral Polio Vaccine - 0 of your ward is due.", "tester.siddhi@gmail.com")