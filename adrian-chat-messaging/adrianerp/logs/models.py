# -*- coding: utf-8 -*-
from __future__ import unicode_literals
 
import datetime

from django.db import models

# Create your models here.
 

class Log(models.Model):
    user = models.CharField(max_length= 200)
    action = models.CharField(max_length= 200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.log 
