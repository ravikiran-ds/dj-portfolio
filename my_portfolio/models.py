from django.db import models
from django import forms

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=254)
    email=models.EmailField(max_length=254)
    msg=models.CharField(max_length=1024)

    def __str__(self):
        return self.name
