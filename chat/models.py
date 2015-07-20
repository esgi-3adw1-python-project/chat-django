from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField(max_length=32)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):

        return self.content
