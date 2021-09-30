from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your  account has been created...')
            print('if')

            return redirect(request, 'users/login.html')

        else:
            print('else')
            form=UserRegistrationForm()

            context={'form' : form}
        return render(request, 'users/register.html', context)



