import Login as xen
import mail_sender as ms
import TTS as tts
print("Welcome to secure login")
if(xen.secure_login()==True):
    print("Logged In")
    service = int(input("1->Bulk mail\n2->TTS"))
    if(service == 1) :
        message = input("Enter your message")
        ms.mail_sender(message)
        tts.TTS(message)
else:
    print("Visit Again")
