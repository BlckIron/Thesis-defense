#!/usr/bin/env python

"""
mailit.py: sending mail with given subject and body

Took inspiration from Corey Schafer's youtube tutorial 
"""
__author__  = "Pedro Barreiros"
__email__   = "pxcodename6@gmail.com"
__credits__ = ["Corey Schafer"]

import os
import smtplib
from decouple import config

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_ADDRESS = config('EMAIL_USER')
EMAIL_PASSWORD = config('EMAIL_PASS')

def send_mail(subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
