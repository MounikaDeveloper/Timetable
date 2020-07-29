from django.db import models

# Create your models here.
class Registration(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)

class TimetableModel(models.Model):
    username=models.CharField(max_length=30)
    weekname=models.CharField(max_length=30)
    t1= models.CharField(max_length=30)
    t2 = models.CharField(max_length=30)
    t3= models.CharField(max_length=30)
    t4 = models.CharField(max_length=30)
    t5= models.CharField(max_length=30)
    t6 = models.CharField(max_length=30)
    t7 = models.CharField(max_length=30)
    t8=models.CharField(max_length=30)
