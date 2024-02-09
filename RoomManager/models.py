from django.db import models


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=255, unique=True)
    room_capacity = models.IntegerField()
    projector = models.BooleanField(default=False)


class RoomManager(models.Model):
    date = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    commentary = models.TextField(blank=True)

    class Meta:
        unique_together = ('room_id', 'date')
        ordering = ('date',)
