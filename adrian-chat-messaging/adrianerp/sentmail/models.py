from django.db import models
from django.conf import settings
from user.models import User

class SentEmail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_receiver')
    subject = models.CharField(max_length=255,default="No Subject")
    message = models.CharField(max_length=5000,default="No Message")
    timestamp = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='uploads',blank=True, null=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
    

    class Meta:
        ordering = ('timestamp',)

   


