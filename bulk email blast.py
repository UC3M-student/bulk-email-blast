import os
import smtplib
import sys

email_address = os.environ.get("user1")
email_password = os.environ.get("pass1")

path = r"C:\Users\merid\Desktop\emails.txt"

with open(path,"r") as file:
    Lines = file.read().splitlines()
print("Sending all emails...")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address,email_password)

    subject = "you just won a huge price"
    body = "You just won 1000 dollars"
    msg = f"Subject: {subject}\n\n{body}"

    n = 0
    while True :
        smtp.sendmail(email_address, Lines[n], msg)
        print("email sent")
        #sys.exit()
        n += 1
        if n > 15:
            sys.exit()


