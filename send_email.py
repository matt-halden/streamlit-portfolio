import smtplib  # used for sending emails
import ssl

host = "smtp.gmail.com"  # standard gmail smtp host
port - 465

username = ""  # enter my app email
password = ""  # app password, not secure, recommended to use environment variables

receiver = ""  # same as username or whatever # we want
context = ssl.create_default_context()

message = """\
Subject: Hi
Hello, test message
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)