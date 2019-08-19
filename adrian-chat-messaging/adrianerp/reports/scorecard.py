from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response


#This holds dummy data ,, when model relating to a handler is given  correct attributes will be fed in
class SiteRework(APIView):
   def get(self,request):
       progress= 30
       return Response({'progress':progress,})
