from django.db import models
from datetime import datetime
# Create your models here.
class Vehical_details(models.Model):
    sap_code=models.CharField(max_length=100)
    ledger_name=models.CharField(max_length=100)
    manufacturer=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    vehical_type=models.CharField(max_length=100)
    base_km=models.CharField(max_length=100)
    rto=models.CharField(max_length=100)


class Engine_details(models.Model):
    model_no=models.CharField(max_length=100)
    chasis=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    old_vehical_no=models.CharField(max_length=100)
    
class Register(models.Model):
    fname = models.CharField(max_length=50,null=True, blank=True)
    lname = models.CharField(max_length=50,null=True, blank=True,default="")
    email = models.EmailField(max_length=255,null=True, blank=True)
    mobile = models.CharField(max_length=12,null=True, blank=True)
    country = models.CharField(max_length=50,null=True, blank=True)
    hobby = models.CharField(max_length=50,null=True, blank=True,default="")
    gender = models.CharField(max_length=15,null=True, blank=True,default="")
    dob = models.CharField(max_length=50,null=True, blank=True, default="")
    image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length=500,null=True, blank=True)
    
    def __str__(self):
        return self.fname #using whole function and fname are which you wants show as object name in admin panel

class Insert_Data(models.Model):
    full_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    date_of_birth = models.CharField(max_length=50, default="")  
    password = models.CharField(max_length=50, default="")  
    def __str__(self):
        return self.full_name  
    
