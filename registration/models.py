from django.db import models

# Create your models here.
from tweepy.models import Model


class Student(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=30)
    email  = models.CharField(max_length=30)
    createdat = models.DateTimeField(auto_now=True);
class StudentsDetails(models.Model):
    address =models.TextField()
    pincode =  models.IntegerField()
    student =models.ForeignKey(Student,on_delete=models.CASCADE)

