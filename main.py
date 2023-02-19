import smtplib
from email.message import EmailMessage
def email_alert(sub, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = sub
    msg['to'] = to

    user = "nksiddhi20@gmail.com"
    msg['from'] = user
    password = 'qknpetgmisshwjur'
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__" :

    email_alert("Invitation", "You are invited for project discussion at 2.00 pm", "nksiddhi20@gmail.com")
    email_alert("Invitation", "You are invited for project discussion at 2.00 pm", "anishpurupawar@gmail.com")
    email_alert("Invitation", "You are invited for project discussion at 2.00 pm", "saniyaatalatti05@com")
    email_alert("Invitation", "You are invited for project discussion at 2.00 pm", "knj1507@hotmail.com")
