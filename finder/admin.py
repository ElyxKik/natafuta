from django.contrib import admin

from finder.models import Avis

# Register your models here.

class AvisAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'photo','nom_complet', 'nom_disparu', 'age', 'is_finded')



admin.site.register(Avis, AvisAdmin)