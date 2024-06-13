from django.urls import path
from .views import PetProfileListCreate, PetProfileDetail

urlpatterns = [
    path('pets/', PetProfileListCreate.as_view(), name='api_pets_list_create'),
    path('pets/<int:pk>/', PetProfileDetail.as_view(), name='api_pets_detail'),
]
