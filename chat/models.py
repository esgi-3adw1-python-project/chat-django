from django.db import models

# Creation du modèle de Message


class Message(models.Model):
    user = models.CharField(max_length=32)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        # Utile pour la partie admin
        return self.content
