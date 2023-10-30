from django.db import models
from frontdesk.models import GuestInfo

# Create your models here.
class Bill(models.Model):
    guest = models.ForeignKey(GuestInfo, on_delete=models.CASCADE)
    total_amount = models.FloatField()

class Payment(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    paid_amount = models.FloatField()