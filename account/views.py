from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from account.models import AgentUser
from account.serializers import UserSerializer, LoginSerializer


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


# API Views.

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        else:
            return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Successfully logged out"}, status=200)




