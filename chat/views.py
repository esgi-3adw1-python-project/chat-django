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

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name=None)
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                template = loader.get_template('index.html')
                return HttpResponse(template.render())
            else:  # sinon une erreur sera affichée
                error = True
                return render(request, 'connexion.html', locals())
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


def inscription(request):
    error = False

    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = User.objects.create_user(username, None, password)
            if user:  # Si l'objet renvoyé n'est pas None
                user = authenticate(username=username, password=password)
                login(request, user)  # nous connectons l'utilisateur
                template = loader.get_template('index.html')
                return HttpResponse(template.render())
            else:  # sinon une erreur sera affichée
                error = True
                return render(request, 'inscription.html', locals())
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())
