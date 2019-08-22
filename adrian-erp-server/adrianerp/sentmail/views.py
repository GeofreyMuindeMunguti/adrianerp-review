from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import SentEmail
from .serializer import  SentEmailSerializer
# Also add these imports
from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class SentEmailViewSet(viewsets.ModelViewSet):
    
    serializer_class = SentEmailSerializer
    queryset = SentEmail.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        query_set = (queryset.filter(sender=self.request.user)|queryset.filter(receiver=self.request.user))
        return query_set
   