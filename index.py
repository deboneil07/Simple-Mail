import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

my_email = os.getenv("MY_EMAIL")
my_pass = os.getenv("MY_PASS")

gmail_server = "smtp.gmail.com"
gmail_port = 587

my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()

my_server.login(my_email, my_pass)

message = MIMEMultipart()

subject = "NEWS"
text_content = "Hello world, this is deboneil07 from antiNET"
message["Subject"] = subject
message.attach(MIMEText(text_content))


my_server.sendmail(
    from_addr= my_email,
    to_addrs= 'db1833@srmist.edu.in',
    msg=message.as_string()
)

my_server.quit()
