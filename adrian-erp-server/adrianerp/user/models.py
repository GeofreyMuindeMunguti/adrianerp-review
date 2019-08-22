from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import datetime
from django.core.cache import cache


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    position = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)
    team = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='uploads', blank=True)

    
    def __str__(self):
        return self.user.username
    
    def last_seen(self):
        return cache.get('last_seen_%s' % self.user.username)
    
    def online(self):
        if self.last_seen():
            now = datetime.datetime.now()
            if now > (self.last_seen() + datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT)):
                return False
            else:
                return True
        else: 
            return False
