from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/sign_up.djt', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/sign_up.djt', {'error': 'Passwords must match.'})
    else:
        return render(request, 'accounts/sign_up.djt')


def sign_in(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/sign_in.djt', {'error': 'Invalid credentials.'})
    else:
        return render(request, 'accounts/sign_in.djt')


def sign_out(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home')
