#SENDING EMAILS WITH PYTHON USINS THE SMTPLIB MODULE

import smtplib

#Send the email with Python
sender =  input("enter the email address of the sender:")
recipient  = input("enter the email address of the recipient:")
msg = input("write the text of the message:")

#Sender credentials
username = input("enter your email address:")
password = input("enter your password to access into your email address account:")

#Sending the email
server = smtplib.SMTP('smtp-mail.outlook.com:587') # with outlook
server.starttls()
server.login(username,password)
server.sendmail(username, recipient, msg)
server.quit()

# server = smtplib.SMTP('smtp.gmail.com:587') # con gmail
# server = smtplib.SMTP('smtp-mail.outlook.com:587') # con outlook
# server =  smtplib.SMTP('smtp.mail.yahoo.com:587') # con yahoo
# server =  smtplib.SMTP('smtp.mail.att.net:465') # con AT&T
# server =  smtplib.SMTP('smtp.comcast.net:465') # con COMCAST
# server =  smtplib.SMTP('smtp.verizon.net:465') # con verizon
# server =  smtplib.SMTP('smtp.mail.yahoo.com:587') # con yahoo