from django.db import models

# Create your models here.

class Room(models.Model):
    #host=
    #topic=
    name= models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)  ## It can be blank. It is same like we do in our accounts where we create our profiles and left few things blank by having a thought that we will fill that out later
    #participants=
    updated= models.DateTimeField(auto_now=True)   ## Time will be updated each time we save 
    created= models.DateTimeField(auto_now_add=True) ## Time will be saved the very first time it was saved

    def __str__(self):
        return self.name