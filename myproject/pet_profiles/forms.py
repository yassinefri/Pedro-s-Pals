from django import forms
from .models import PetProfile

class PetProfileForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['owner', 'name', 'age', 'species', 'breed', 'description', 'photo']
