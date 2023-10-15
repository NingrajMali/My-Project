from django.db import models

# Create your models here.
from django.db import models 
from django.contrib.auth import authenticate, login as LOGIN, logout as LOGOUT
from django.contrib import messages
# Create your views here.

class signup(models.Model):
    first_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Mobile_No=models.CharField(max_length=12)
    Password=models.CharField(max_length=50)
    Confirm_Password=models.CharField(max_length=50) 


class login(models.Model):
    usrname=models.CharField(max_length=50)
    pasword=models.CharField(max_length=30)
