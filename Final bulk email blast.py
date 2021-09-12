import os
import smtplib
from email.message import EmailMessage
import imghdr

email_address = os.environ.get("user1")
email_pass = os.environ.get("pass1")

msg = EmailMessage()
msg["Subject"] = "Check out this new song"
msg["From"] = email_address

msg.set_content("https://www.youtube.com/watch?v=7zp1TbLFPp8&ab_channel=DonOmarVEVO")


#SEND ATTACHED IMAGES  IN THE EMAIL

#photo_path = r"C:\Users\mer..."
#with open(photo_path, "rb") as f:
 #   file_data = f.read()
 #   file_type = imghdr.what(f.name)
 #   file_name = f.name

#msg.add_attachment(file_data, maintype="image", subtype=file_type, file_name= file_name)

#Method to send individuals emails

path = r"C:\Users\merid\Desktop\emails.txt"
with open(path,"r") as file :
    Lines = file.read().splitlines()
print("Loading all emails")
n = 0

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp :
    smtp.login(email_address,email_pass)
    for email in Lines :
        msg["To"] = email
        smtp.send_message(msg)
        n += 1
        print("email sent number:", n)
        del msg["To"]

