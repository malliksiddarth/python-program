#!/usr/bin/python3
import smtplib 
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls() 
server.login("malliksiddarth239@gmail.com","9980521996")
msg="BAhubali"
server.sendmail("malliksiddarth239@gmai.com","malliksiddarth239@gmail.com",msg) 
print("success")
server.quit()