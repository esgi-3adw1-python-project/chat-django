from django import forms

#  Creation du formulaire de connexion, inscription et du chat


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=32)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=32)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="", max_length=255)



