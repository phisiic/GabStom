from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect('homepage:homepage')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('email')
                messages.success(request, 'Konto utworzono dla użytkownika ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage:homepage')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage:homepage')
            else:
                messages.info(request, 'Błędny adres email lub hasło')

        context = {}
        return render(request, 'login.html', context)


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return redirect('accounts:login')