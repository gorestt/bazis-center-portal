
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts.models import Profile
from .forms import LoginForm, CreateUserForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:home')
    else:
        form = LoginForm(request)
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('core:index')

@login_required
def user_create(request):
    profile = getattr(request.user, 'profile', None)
    role = profile.role if profile else ('admin' if request.user.is_superuser else 'client')
    if role != 'admin':
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden('Доступ запрещён.')
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            if form.cleaned_data.get('role') in ['admin', 'manager']:
                user.is_staff = True
            if form.cleaned_data.get('role') == 'admin':
                user.is_superuser = True
            user.save()
            Profile.objects.create(user=user, role=form.cleaned_data['role'])
            return redirect('dashboard:home')
    else:
        form = CreateUserForm()
    return render(request, 'accounts/user_create.html', {'form': form})
