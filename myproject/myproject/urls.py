"""
URL configuration for myproject project.

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
from django.urls import path
from django.urls import include, path
from django.contrib.auth import views as auth_views
from pet_profiles import views as pet_profiles_views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include('pet_profiles.urls')),
     path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', pet_profiles_views.signup, name='signup'),  # Ajout du chemin pour l'inscription
    path('accounts/', include('django.contrib.auth.urls')),
    path('messaging/', include('messaging.urls')),
    path('', pet_profiles_views.index, name='home'),
]
