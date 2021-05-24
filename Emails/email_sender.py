import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('./Emails/index.html').read_text())
email = EmailMessage()

email = EmailMessage()
email['from'] = 'Lance Parantar'
email['to'] = 'gaminglance11@gmail.com'
email['subject'] = 'You won 1,000,000 Dollars!'

email.set_content(html.substitute(name='Tintin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<YOUR EMAIL>', '<PASSWORD>')
    smtp.send_message(email)
    print('Send Successfully!')
