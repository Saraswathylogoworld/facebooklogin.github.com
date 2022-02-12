from django.db import models

# Create your models here.
class freg(models.Model):
    fname = models.CharField(max_length=200,null=True,blank=False) 
    lname = models.CharField(max_length=200,null=True,blank=False) 
    password = models.CharField(max_length=200,null=True,blank=False)
    email = models.CharField(max_length=200,null=True,blank=False)
    date = models.IntegerField(null=True,blank=False) 
    month = models.CharField(max_length=200,null=True,blank=False) 
    year = models.IntegerField(null=True,blank=False) 
    gender = models.CharField(max_length=200,null=True,blank=False)