from django import forms
from .models import PetProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['owner', 'name', 'age', 'species', 'breed', 'description', 'photo']

        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)