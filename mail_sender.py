import smtplib, ssl ,random

def mail_sender(message):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "xensprofessionalbeta@gmail.com"
    password = input("Type your password and press enter:")

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        receiver_list = ["xensprofessionalbeta@gmail.com"]
        for receiver_email in  receiver_list :
            server.sendmail(sender_email, receiver_email, message)

    print("Message sent")
    return
