"""
URL configuration for natafuta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from finder.views import home, contact, avis_recherche, retrouves, new_avis, avis_detail, personne_retrouve, recherche, mon_compte
from account.views import user_login, signup, logout_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', home, name='home'),
    path('avis_recherche', avis_recherche, name='avis_recherche'),
    path('personnes-retrouves', retrouves, name='retrouves'),
    path('contact', contact, name='contact'),
    path('new-avis', new_avis, name='new_avis'),
    path('personne_retrouve/<int:id>', personne_retrouve, name='personne_retrouve'),
    path('avis-detail/<int:id>', avis_detail, name='avis_detail'),
    path('compte', mon_compte, name='mon_compte'),
    path('recherche', recherche, name='recherche'),
    path('login', user_login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout_user, name='logout')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
