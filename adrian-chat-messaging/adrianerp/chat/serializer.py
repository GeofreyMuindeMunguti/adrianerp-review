from user.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Message
 

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='email', queryset=User.objects.all())

    

    class Meta:
        model = Message
        fields = ['url','sender', 'receiver', 'message', 'timestamp']
