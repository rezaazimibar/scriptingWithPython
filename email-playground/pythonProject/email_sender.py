import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

gmail_user = 'lastknight490@outlook.com'
gmail_app_password = 'jTrEEk2YL7LRgAW'
html = Template(Path('index.html').read_text())
# print(html.substitute(name="hey")) this way we can give a value to only one variable

my_email = EmailMessage()
my_email['from'] = 'lastknight490@outlook.com'
my_email['to'] = 'lastknight490@gmail.com'
my_email['subject'] = 'you nothing bro I am sorry'

# my_email.set_content('this is the long text as')  #--if we want to send just a simple text
my_email.set_content(html.substitute({'name': "andre bozo"}), 'html ')  # this way we can add multiple value

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(gmail_user, gmail_app_password)
    smtp.send_message(my_email)
    print("all went good👍👍")
