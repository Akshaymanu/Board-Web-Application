from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    age =  models.TextField(null=True,blank=True)
    job = models.CharField(max_length=100,null=True)
    location = models.CharField(max_length=100,null=True,blank=True)

    
    def __str__(self):
        return self.host

class Topic(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL , null=True)  
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']   # displaying first the newest items that  created  or updated on top 

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.body[0:50]    # preview  the first 50 characters...

