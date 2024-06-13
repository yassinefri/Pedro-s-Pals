from django.urls import path
from . import views
from .views import PetProfileListCreate, PetProfileDetail

app_name = 'pet_profiles'
urlpatterns = [
     path('api/pets/', PetProfileListCreate.as_view(), name='petprofile-list-create'),
    path('api/pets/<int:pk>/', PetProfileDetail.as_view(), name='petprofile-detail'),
    path('', views.index, name='index'),
    path('<int:pet_id>/', views.detail, name='detail'),
    path('create/', views.create_pet_profile, name='create_pet_profile'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('swipe/', views.swipe_pets, name='swipe'), 
]
