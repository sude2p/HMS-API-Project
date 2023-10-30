from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

class Food(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)