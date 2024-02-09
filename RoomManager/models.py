from django.db import models


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_capacity = models.IntegerField()
    projector = models.BooleanField(default=False)
