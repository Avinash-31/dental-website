from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class appointments(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length = 254,null=True)
    mobile = models.CharField(max_length=13,null=True)
    address = models.CharField(max_length=254)
    dateOfAppointment = models.DateField(max_length=20,null=False)
    timestamp = models.DateTimeField()
    msg = models.CharField(max_length=1000,null = True)
    slot = models.CharField(max_length = 20,default = "Select your preferred slot")
   
    def __str__(self):
        return self.name
    
class contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length = 254,null=True)
    msg = models.CharField(max_length=1000,null = True)
    
    def __str__(self):
        return self.name
