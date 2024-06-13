from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import PetProfile
from .forms import PetProfileForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

def index(request):
    pet_profiles = PetProfile.objects.all()
    return render(request, 'pet_profiles/index.html', {'pet_profiles': pet_profiles})

def detail(request, pet_id):
    pet = get_object_or_404(PetProfile, pk=pet_id)
    return render(request, 'pet_profiles/detail.html', {'pet': pet})

@login_required
def create_pet_profile(request):
    if request.method == 'POST':
        form = PetProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pet_profiles:index'))
    else:
        form = PetProfileForm()
    return render(request, 'pet_profiles/create_pet_profile.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        results = PetProfile.objects.filter(
            Q(name__icontains=query) | 
            Q(species__icontains=query) | 
            Q(breed__icontains=query)
        )
    else:
        results = PetProfile.objects.all()
    return render(request, 'pet_profiles/search.html', {'results': results, 'query': query})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        else:
            error_message = ' '.join([' '.join(e) for e in form.errors.values()])
            messages.error(request, error_message)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup_login.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'username': request.user.username})
    else:
        return render(request, 'home.html', {'username': None})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'registration/signup_login.html', {'view': 'login'})
    return render(request, 'registration/signup_login.html', {'view': 'login'})

def logout_view(request):
    logout(request)
    return redirect('login')
