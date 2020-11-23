# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:21:43 2020

@author: hugo1
"""
import smtplib
gmail_user = 'jardindepluiegbx@gmail.com'
gmail_password = 'pythonwasabi'
        
sent_from = gmail_user
to = 'hugo1199@hotmail.com'
    
subject = 'alerte'
body = 'test'
    
email_text = """\
From: %s
To: %s
Subject: %s
        
%s
""" % (sent_from, ", ".join(to), subject, body)
        
try:
         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
         server.ehlo()
         server.login(gmail_user, gmail_password)
         server.sendmail(sent_from, to, email_text)
         server.close()
        
         print ('Email sent!')
except:
         print ('Something went wrong...')