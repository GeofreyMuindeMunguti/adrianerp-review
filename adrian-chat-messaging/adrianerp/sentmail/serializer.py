from rest_framework import serializers
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.mail.message import EmailMessage
from .models import SentEmail
from emailserver.models import EmailConfig
from django.db.models.signals import post_save
from django.dispatch import receiver
import traceback
import sys, os
from logs.models import Log
from django.core.mail import get_connection
 

class SentEmailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SentEmail
        fields = ('url','sender','receiver', 'subject', 'message','attachment')
        
        @receiver(post_save,sender=SentEmail)
        def send_email(instance,**kwargs):
         server = EmailConfig.objects.order_by('email_host').first()
         my_host = server.email_host
         my_port = server.sender_port
         my_username = server.email_host_user
         my_password = server.email_host_password
         my_use_tls = server.email_use_tls
        
         connection = get_connection(host=my_host, 
                            port=my_port, 
                            username=my_username, 
                            password=my_password, 
                            use_tls=my_use_tls) 
         try:
          email = EmailMessage(instance.subject,instance.message,my_username,[instance.receiver.email], connection=connection)
          email.attach_file(str(instance.attachment))
          email.send()
          newlog = Log(user=instance.sender.email, action="emailmessage/create")
          newlog.save()

         except Exception:
             traceback.print_exc()
        
         def create(self, validated_data):
          message = EmailMessage(**validated_data)
          sender = validated_data.pop('sender')
          message.save()
          return message
       
         
         
        
        
        

 