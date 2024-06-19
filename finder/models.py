from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from django.dispatch import receiver

from PIL import Image
from account.models import AgentUser


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
    is_refugee = models.BooleanField(default=False)
    is_deplacee = models.BooleanField(default=False)

@receiver(pre_save, sender=Avis)
def resize_image(sender, instance, **kwargs):
    if instance.photo:
        img = Image.open(instance.photo)
        img.thumbnail((500, 500), Image.Resampling.LANCZOS)
        img.save(instance.photo.path)



