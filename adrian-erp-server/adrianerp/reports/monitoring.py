from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response



class MileStoneStatus(APIView):
   #This holds dummy data ,, when model relating to a handler is given  correct attributes will be fed in
 def get(self,request):
    total_sites    = 0 #total count of sites 
    sites_accepted = 0 # total count of sites accepted
    sites_rejected = total_sites - sites_accepted 
    return Response ({'total_sites':total_sites,'sites_accepted':sites_accepted,'sites_rejected':sites_rejected})


##Still 
#This holds dummy data ,, when model relating to a handler is given  correct attributes will be fed in
class BudgetStatus(APIView):
    def get(self,request):
        return Response({})