from tkinter import CASCADE

from django.db import models

# Create your models here.
class Userregister_Model(models.Model):
    name= models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
    phoneno=models.CharField(max_length=15)
    address=models.CharField(max_length=500)
    location=models.CharField(max_length=20)


class UserAdd_Model(models.Model):
    uregid = models.ForeignKey(Userregister_Model, on_delete=CASCADE)
    cname = models.CharField(max_length=100)
    dept = models.CharField(max_length=10000)
    description = models.CharField(max_length=1000)
    website=models.CharField(max_length=1000)
    method = models.CharField(max_length=100)
    record = models.CharField(max_length=500)
    attackresult = models.CharField(max_length=500)

