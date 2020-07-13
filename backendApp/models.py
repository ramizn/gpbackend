from django.db import models

# Create your models here.
class Driver(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=500, default="")
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=30)
    city = models.CharField(max_length=30, null=True)
    phoneNo = models.CharField(max_length=14)
    carType = models.CharField(max_length=1,default="f") #f=> fuel /e=> electrical



