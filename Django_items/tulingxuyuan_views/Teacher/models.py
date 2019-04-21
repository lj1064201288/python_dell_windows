from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=20)


# Create your models here.
