from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from logs.models import Log
from .models import Message
from chat.serializer import  MessageSerializer
# Also add these imports
from user.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class ChatViewSet(viewsets.ModelViewSet):
    
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    def get_queryset(self):
     queryset = self.queryset
     query_set = (queryset.filter(sender=self.request.user)|queryset.filter(receiver=self.request.user))
     return query_set
