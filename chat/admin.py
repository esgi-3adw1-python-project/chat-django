from django.contrib import admin
from chat.models import Message

# On affiche le mod�le de Message dans la partie admin


admin.site.register(Message)
