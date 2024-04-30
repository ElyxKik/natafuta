from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from account.models import AgentUser


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger l'utilisateur vers une page après la connexion
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire HTML personnalisé
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Créer un nouvel utilisateur
        user = AgentUser.objects.create_user(username=username, password=password)
        # Rediriger l'utilisateur vers une page après l'inscription
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'signup.html')
    

def logout_user(request):
    logout(request)
    return redirect('login')


# Create your views here.

