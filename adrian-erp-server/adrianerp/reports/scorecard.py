from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response


#This holds dummy data ,, when model relating to a handler is given  correct attributes will be fed in
class SiteRework(APIView):
   def get(self,request):
       totalIssues = Issues.objects.all().count()
       totalIssuesRejected =Issues.objects.filter(issue_image__isnull=False).count()
       totalIssuesUndefined = totalIssues - totalIssuesRejected
       return Response({'total issues':totalIssues,'site rework total':totalIssuesRejected,'total issues undefined':totalIssuesUndefined})


