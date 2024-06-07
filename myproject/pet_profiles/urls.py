from django.urls import path
from . import views

app_name = 'pet_profiles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pet_id>/', views.detail, name='detail'),
    path('create/', views.create_pet_profile, name='create_pet_profile'),
]