from django import forms
from .models import PetProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['owner', 'name', 'age', 'species', 'breed', 'description', 'photo']

        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("L'utilisateur existe déjà. Veuillez choisir un autre nom d'utilisateur.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé. Veuillez en choisir un autre.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas. Veuillez réessayer.")
        return password2