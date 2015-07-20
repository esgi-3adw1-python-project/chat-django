from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader

from django.contrib.auth import authenticate, login

from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from chat.forms import ConnexionForm
from chat.forms import InscriptionForm
from chat.forms import MessageForm

from chat.models import Message

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name=None)
def home(request):
    request.user  # On récupère les infos du user connecté
    last_messages = Message.objects.order_by('-date')  # On récupère tous les messages
    if request.method == "POST":  # Si le formulaire a été envoyé
        form = MessageForm(request.POST)  # On récupère le formulaire choisi
        if form.is_valid():
            pseudo = request.user.username  # On récupère le pseudo du user connecté
            msg = request.POST.get('message', '')  # On récupère le message du formulaire
            message = Message.objects.create(user=pseudo, content=msg)  # On insère en base
            if message:  # Si l'objet renvoyé n'est pas None
                last_messages = Message.objects.order_by('-date')
            else:  # Sinon une erreur sera affichée
                error = True
    else:
        form = MessageForm()  # On affiche le formulaire choisi
    return render(request, 'index.html', locals())


def connexion(request):
    error = False  # On initialise la variable d'erreur

    if request.method == "POST":   # Si le formulaire a été envoyé
        form = ConnexionForm(request.POST)  # On récupère le formulaire choisi
        if form.is_valid():
            username = request.POST.get('username', '')  # On récupère le pseudo du formulaire
            password = request.POST.get('password', '')  # On récupère le password du formulaire
            user = authenticate(username=username, password=password)  # On l'objet du user
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # On connecte le user
                return redirect(reverse(home))  # Redirection vers l'index
            else:  # Sinon une erreur sera affichée
                error = True
                return render(request, 'connexion.html', locals())
    else:
        form = ConnexionForm()  # On affiche le formulaire choisi

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)  # On déconnecte le user
    return redirect(reverse(connexion))  # Redirection vers la vue de connexion


def inscription(request):
    error = False  # On initialise la variable d'erreur

    if request.method == "POST":   # Si le formulaire a été envoyé
        form = InscriptionForm(request.POST)  # On récupère le formulaire choisi
        if form.is_valid():
            username = request.POST.get('username', '')  # On récupère le pseudo du formulaire
            password = request.POST.get('password', '')  # On récupère le password du formulaire
            user = User.objects.create_user(username, None, password)  # On inscrit le user
            if user:  # Si l'objet renvoyé n'est pas None
                user = authenticate(username=username, password=password)  # On récupère l'objet du user
                login(request, user)  # On connecte le user

                return redirect(reverse(home))  # Redirection vers l'index
            else:  # Sinon une erreur sera affichée
                error = True
                return render(request, 'inscription.html', locals())
    else:
        form = InscriptionForm()  # On affiche le formulaire choisi

    return render(request, 'inscription.html', locals())
