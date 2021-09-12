import os
import smtplib
from email.message import EmailMessage
import imghdr


email_address = os.environ.get("user1")
email_pass = os.environ.get("pass1")

msg = EmailMessage()
msg["Subject"] = "Check out my new album!"
msg["From"] = email_address
msg["To"] = email_address
msg.set_content("You can´t believe what I just heard -> \n this is crazy \n It has blown my mind\n check it out \n https://www.youtube.com/watch?v=s4qnWuBpjAs&ab_channel=Tubon-Topic" )

photo_path= r"C:\Users\merid\Desktop\music_record.jpg"
with open(photo_path, "rb") as f :
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)


with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email_address,email_pass)
    smtp.send_message(msg)

print("image sent")
