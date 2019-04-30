import time
from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)

    def curTime(self):
        return  time.time()

    curTime.short_description = '当前时间'
    curTime.admin_order_field = 'name'

    room = models.OneToOneField(ClassRoom)

    def __str__(self):
        return self.name

    def getRoom(self):
        return self.room.roomName

    getRoom.short_description = '教室'

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom)

    def __str__(self):
        return self.name

