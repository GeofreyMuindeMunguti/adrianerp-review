from rest_framework import serializers
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import EmailConfig
 

class EmailConfigSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmailConfig
        fields = ['url','email_host', 'sender_port', 'email_host_user','email_host_password', 'email_use_ssl','email_use_tls']
        extra_kwargs = {'email_host_password': {'write_only': True}}

 