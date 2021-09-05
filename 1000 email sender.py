import os
import smtplib

email_address = os.environ.get("user1")
email_password = os.environ.get("pass1")

#emails file

path = r"C:\Users\merid\Desktop\emails.txt"

with open(path,"r") as file:
    Lines = file.read().splitlines()
print(Lines)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_address,email_password)

    subject = "you just won a huge price"
    body = "You just won 1000 dollars"
    msg = f"Subject: {subject}\n\n{body}"

    for i in Lines :
        smtp.sendmail(email_address, Lines, msg)
        file.close()
        print("email sent")



