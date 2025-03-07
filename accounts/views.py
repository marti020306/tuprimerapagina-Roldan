from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserUpdateForm, ProfileForm
from .models import Profile

# 🟢 REGISTRO DE USUARIO
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  
    else:
        form = CustomUserCreationForm()
    
    return render(request, "accounts/register.html", {"form": form})

# 🟢 LOGIN Y LOGOUT
def logout_view(request):
    logout(request)
    return redirect('post_list')

# 🟢 PERFIL DE USUARIO
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

# 🟢 EDITAR PERFIL
@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Asegura que el perfil existe
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():        
            form.save()
            return redirect("profile")  
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, "accounts/edit_profile.html", {"form": form})

# 🟢 CAMBIAR CONTRASEÑA
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})
