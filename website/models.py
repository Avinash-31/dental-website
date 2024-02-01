from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class appointment(models.Model):
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
    
class pricing(models.Model):
    service_name = models.CharField(max_length=128)
    stage = models.CharField(max_length = 128,null=False)
    price = models.CharField(max_length=13,null=False)
   
    def __str__(self):
        return self.service_name

class dentist(models.Model):
    dentist_name = models.CharField(max_length=128)
    designation = models.CharField(max_length = 128,null=True)
    facebook_link = models.CharField(max_length = 128,null=True)
    instagram_link = models.CharField(max_length = 128,null=True)
    email_link = models.CharField(max_length = 128,null=True)
    image = models.ImageField(upload_to='images', blank=True)
    
   
    def __str__(self):
        return self.dentist_name
    
class review(models.Model):
    customer_name = models.CharField(max_length=128)
    msg = models.CharField(max_length = 128,null=True)
    profession = models.CharField(max_length = 128,null=True)
   
    def __str__(self):
        return self.customer_name
