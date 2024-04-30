from django.db import models
from account.models import AgentUser
from django.db.models.deletion import CASCADE
# Create your models here.


class Avis(models.Model):
    user = models.ForeignKey(AgentUser, on_delete=CASCADE)
    nom_complet = models.CharField(max_length=200)
    nom_disparu = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="photo/")
    age = models.IntegerField()
    sexe = models.CharField(max_length=6)
    telephone = models.IntegerField()
    province = models.CharField(max_length=200)
    lieu_disparition = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)
    description = models.TextField()
    date_disparition = models.DateField()
    date_finded = models.DateField(null=True)
    created_time = models.DateTimeField(auto_now=True)
    is_finded = models.BooleanField(default=False)



