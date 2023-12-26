from email.message import EmailMessage
import ssl
import smtplib

password = 'vnja luss diyg pxlz' 

emails = [
    'praiseoyegue53@gmail.com',
    'bilon36786@wikfee.com',
    'anthonyjubemi@gmail.com',
    'jubemi.pajiah@eng.uniben.edu',
    'edafevictor67@gmail.com',
    'mhizteeomat@gmail.com',
    'erhisohwodegratefulruki@gmail.com',
    'pajiahjames@gmail.com',
    'joelpajiah@gmail.com'
]

for receiver in emails:
    email_sender = 'jubemipajiah@gmail.com'
    email_password = password
    email_receiver = receiver
    subject = 'This is From Python'
    body= """
    This is my third mail from Python. If you see this, Be prepared for more. This is a loop and the loop ought to run 9 times. Meaning I'm going to send this mail to 9 people at once using python.
    It doesn't mean that you'll receive it 9 times, It just means that you and 9 other people will get it at once.
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())