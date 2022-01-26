from django.shortcuts import render, redirect

import smtplib
import ssl
from email.message import EmailMessage

from decouple import config # for converting .env file

# Create your views here.


def index(request):
    
    if request.method=='POST':
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # msg_body=request.POST.get('msg_body')
        # print(email)
        # print(subject)
        # print(msg_body)

        # sender email is coming from .env file
        sender_email=config('sender_email') #company email 
        password=config('password')

        # detail enter by user window - html form
        receiver_email=request.POST.get('email')
        receiver_subject=request.POST.get('subject')
        body=request.POST.get('msg_body')

        # message setting area
        message=EmailMessage()
        message['From']=sender_email
        message['To']=receiver_email
        message['Subject']=receiver_subject
        # message.set_content(body)

        html = f"""
        <html>
            <body>
                <h1>{receiver_subject}</h1>
                <h4>{body}</h4>
            </body>
        </html>
        """

        message.add_alternative(html, subtype="html")

        context=ssl.create_default_context() # it securing connection

        print('Sending Email')

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print('Success')

        # return render(request,'index.html',{'send':"Message send succesfully"})
        return redirect(sended)


    return render(request,'index.html',{})



def sended(request):
    
    return render(request,'index.html',{'send':'Message send succesfully'})