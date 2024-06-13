from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from pet_profiles import views as pet_profiles_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include('pet_profiles.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/signup_login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', pet_profiles_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('messaging/', include('messaging.urls')),
    path('', pet_profiles_views.index, name='home'),
]
