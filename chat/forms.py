from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=32)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=32)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)



