from django.db import models
from django.contrib import admin
import datetime

class Person(models.Model):
    Name = models.TextField() # Имя пользователя 
    Surname = models.TextField() # Фамилия 
    Birthday = models.DateField(default=datetime.datetime.now())
    Password = models.TextField()
    Login = models.TextField()


class BloodMeasurement(models.Model):
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Date = models.DateField(default=datetime.date.today())
    TypeMeasurement = models.PositiveSmallIntegerField() 
    DataMeasurement = models.FloatField() 



# Create your models here.
