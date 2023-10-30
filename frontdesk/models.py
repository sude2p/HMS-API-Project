from django.db import models

# Create your models here.
class GuestInfo(models.Model):
    f_name = models.CharField(max_length=100 , blank=False,null=False)
    l_name = models.CharField(max_length=100 , blank=False,null=False)
    address =models.TextField(blank = False , null = False)
    phone_number = models.IntegerField()
    email = models.EmailField(default='@mailid.com',unique=True)

class RoomType(models.Model):
    name = models.CharField(max_length=100) 

class Room(models.Model):
    room_status =[('Occupied','Occupied'),('Available','Available')]
    room_no = models.IntegerField(blank=False , null = False)
    description = models.TextField(null=True)
    status = models.CharField(max_length=100, choices=room_status)
    floor = models.CharField(max_length =100, blank=False , null=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL,null=True)

class GuestRoom(models.Model):
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
