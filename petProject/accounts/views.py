from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegisterForm

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('')  
        else:

            form = AuthenticationForm()
            return redirect('login')
    return render(request, 'accounts/login.html', {'form': form})


class RegisterView(CreateView):

    form_class = RegisterForm

    template_name = 'accounts/register.html'

    success_url = reverse_lazy('login')

