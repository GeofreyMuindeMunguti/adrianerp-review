from django.db import models
from django.conf import settings


class EmailConfig(models.Model):
    email_host = models.CharField(max_length=1200)
    sender_port = models.IntegerField()
    email_host_user = models.CharField(max_length=1200)
    email_host_password = models.CharField(max_length=1200)
    email_use_ssl =models.BooleanField(default=False)
    email_use_tls = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email_host

   


