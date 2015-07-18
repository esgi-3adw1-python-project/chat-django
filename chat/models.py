from django.db import models

# Create your models here.

class Message(models.Model):
    user = models.CharField(max_length=32)
    content = models.TextField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.user
