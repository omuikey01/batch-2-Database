from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    claass = models.IntegerField()
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    fess = models.IntegerField()
    