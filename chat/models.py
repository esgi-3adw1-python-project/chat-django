from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    date = models.DateTimeField('date published')
