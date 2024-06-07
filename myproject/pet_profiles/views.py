from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PetProfile
from .forms import PetProfileForm

def index(request):
    pet_profiles = PetProfile.objects.all()
    return render(request, 'pet_profiles/index.html', {'pet_profiles': pet_profiles})

def detail(request, pet_id):
    pet = get_object_or_404(PetProfile, pk=pet_id)
    return render(request, 'pet_profiles/detail.html', {'pet': pet})

def create_pet_profile(request):
    if request.method == 'POST':
        form = PetProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet_profiles:index'))
    else:
        form = PetProfileForm()
    return render(request, 'pet_profiles/create_pet_profile.html', {'form': form})
