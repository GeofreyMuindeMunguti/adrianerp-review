from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import EmailConfig
from .serializer import  EmailConfigSerializer
# Also add these imports
from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class EmailConfigViewSet(viewsets.ModelViewSet):
    
    serializer_class = EmailConfigSerializer
    queryset = EmailConfig.objects.all()
   
   