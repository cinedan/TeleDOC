###
# This file will send email using credential in json file
#
# NOTE: Requires email_creds.json,
#       see email_creds.json.sample
###


# smtplib module send mail
import smtplib
import json
import os
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys

# format for time sent in email
TIME_STR_FORMAT = '%l:%M%p %Z on %b %d, %Y'

def send_email(send_to, subject, text):
    """
    send an email
    """
    # read credentials
    with open(os.getcwd() + "/email_creds.json") as cred_file:
        cred_dict = json.load(cred_file)

    # insert credentials to variables
    sender_email = list(cred_dict.keys())[0]
    sender_password = cred_dict[sender_email]

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = send_to

    success = False
    msg = make_plain_msg(msg, text)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        # Gmail Sign In
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)

        # send email
        server.sendmail(sender_email, [send_to], msg.as_string())
        print('email sent')
        success = True
    except:
        print('error sending mail')
    finally:
        server.quit()

    return success


def load_image_with_body(msg, text, image_link):
    """
    load image inside HTML body along with text
    """
    img_html = "<br><img src=" + image_link + "><br>"


    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
            """ + time.strftime(TIME_STR_FORMAT) + """<br>
            """ + text + """
        </p>""" + img_html + """
        <p><br>
        Thank You,<br>
        Team TimeClockPi        
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(html, 'html'))

    return msg


def make_plain_msg(msg, text):
    """
    load text inside HTML body only
    """
    html = text

    msg.attach(MIMEText(html, 'html'))

    return msg


if __name__ == "__main__":
    
    send_email(sys.argv[1], sys.argv[2], sys.argv[3])
