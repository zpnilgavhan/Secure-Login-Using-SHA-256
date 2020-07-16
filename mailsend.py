import smtplib, ssl ,random

def sendemail():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "xensprofessionalbeta@gmail.com"
    receiver_email = "xensprofessionalbeta@gmail.com"
    #password = input("Type your password and press enter:")
    password = "Beta@123"
    message = """\
    Subject: Hi there

    This message is sent from Python.
    Your OTP is """
    otp = (str)(random.randint(1000, 9999))
    message += otp

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("DONE")
