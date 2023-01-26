from django.db import models

# Create your models here.
class login(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    type = models.TextField(max_length=30)

class home(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    number = models.IntegerField()
    message = models.CharField(max_length=200)

class driver(models.Model):
    fullname=models.CharField(max_length=30)
    cnic=models.IntegerField()
    email = models.EmailField(max_length=30)
    workarea=models.CharField(max_length=30)
    cardn=models.IntegerField()
    cvc=models.IntegerField()
    expm=models.IntegerField()
    expy=models.IntegerField()

class truck(models.Model):
    truckc=models.CharField(max_length=30)
    truckt=models.CharField(max_length=30)
    truckn=models.CharField(max_length=30)

class order(models.Model):
    truckc=models.CharField(max_length=30)
    truckt=models.CharField(max_length=30)
    truckn=models.CharField(max_length=30)

class rating(models.Model):
    username=models.CharField(max_length=30)
    dname=models.CharField(max_length=30)
    rating=models.IntegerField()
