from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from finder.models import Avis
from account.models import AgentUser
from finder.serializers import AvisSerializer

# Create your views here.

def home(request):
    avis_recherche = Avis.objects.all()
    avis = Avis.objects.filter(is_finded=False).order_by('-created_time')[:3]
    nombre_avis = avis_recherche.count()
    avis_resolu = Avis.objects.filter(is_finded=True).order_by('-created_time')[:3]
    nombre_avis_resolu = avis_resolu.count()
    agent = AgentUser.objects.all().count()
    return render(request, 'home.html', {'avis':avis, 
                                         'avis_recherche':avis_recherche,
                                         'nombre_avis':nombre_avis, 
                                         'nombre_avis_resolu':nombre_avis_resolu,
                                         'avis_resolu':avis_resolu,
                                         'agent': agent})


def avis_recherche(request):
    avis = Avis.objects.filter(is_finded=False)
    return render(request, 'avis.html', {'avis':avis})


def avis_detail(request, id):
    avis = get_object_or_404(Avis, id=id)
    avis_similaire = Avis.objects.filter(province=avis.province, is_finded=False).exclude(id=id)
    return render(request, 'avis-detail.html', {'avis':avis, 'avis_similaire':avis_similaire})


def mon_compte(request):
    user = request.user
    avis = Avis.objects.filter(user=user)
    return render(request, 'mon-compte.html', {'avis': avis})


def recherche(request):
    if request.method == 'POST':
        query = request.POST.get('recherche')
        avis = Avis.objects.filter(nom_disparu__icontains=query)
        return render(request, 'resultat.html', {'avis':avis, 'query':query})

def retrouves(request):
    avis_resolu = Avis.objects.filter(is_finded=True)
    return render(request, 'retrouves.html', {'avis_resolu':avis_resolu})

def personne_retrouve(request, id):
    avis = Avis.objects.get(id=id)
    avis.is_finded = True
    avis.date_finded = datetime.now()
    avis.save()
    return redirect('avis_detail', id)


def contact(request):
    return render(request, 'contact.html')


def new_avis(request):
    user = request.user
    if request.method == 'POST':
        nom_complet = request.POST.get('nom_complet')
        nom_disparu = request.POST.get('nom_disparu')
        photo = request.FILES.get('photo')
        date_disparition = request.POST.get('date_disparition')
        age = request.POST.get('age')
        sexe = request.POST.get('sexe')
        telephone = request.POST.get('telephone')
        province = request.POST.get('province')
        lieu_disparition = request.POST.get('lieu_disparition')
        adresse = request.POST.get('adresse')
        description = request.POST.get('description')
        avis = Avis.objects.create(user=user,
                                   nom_complet=nom_complet, 
                                   nom_disparu=nom_disparu,
                                   photo = photo,
                                   date_disparition=date_disparition,
                                   age=age, 
                                   sexe=sexe, 
                                   telephone=telephone,
                                   province=province,
                                   lieu_disparition=lieu_disparition,
                                   adresse=adresse,
                                   description=description 
                                   )
        avis.save()
        return redirect('home')
    



class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.all()
    serializer_class = AvisSerializer

    @action(detail=False, methods=['get'], url_path='stats')
    def stats(self, request):
        total_avis = Avis.objects.count()
        avis_retrouves = Avis.objects.filter(is_finded=True).count()

        data = {
            'nombre_avis': total_avis,
            'nombre_retrouve': avis_retrouves
        }

        return Response(data)