from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topics(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic= models.ForeignKey(Topics, on_delete=models.SET_NULL, null=True)
    name= models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)  ## It can be blank. It is same like we do in our accounts where we create our profiles and left few things blank by having a thought that we will fill that out later
    participants= models.ManyToManyField(User,related_name='participants', blank=True)
    updated= models.DateTimeField(auto_now=True)   ## Time will be updated each time we save the model
    created= models.DateTimeField(auto_now_add=True) ## Time will be saved the very first time it was saved

    class Meta:
        ordering= ['-updated', '-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user= models.ForeignKey(User ,on_delete=models.CASCADE)
    room= models.ForeignKey(Room ,on_delete=models.CASCADE)
    body= models.TextField()
    updated= models.DateTimeField(auto_now=True)   ## Time will be updated each time we save the model
    created= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-created']

    def __str__(self):
        return self.body[0:50]