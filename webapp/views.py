from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db import transaction
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .form import *
from social_django.utils import psa, load_strategy
from django.contrib.auth import get_user_model
UserModel = get_user_model()

def index(request):
    context = {}
    return render(request, 'index.html', context)

def account(request):
    context = {}
    return render(request, 'account.html', context)

def feed(request):
    context = {}
    return render(request, 'feed.html', context)

def login(request):
    form=UserForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
                if user.is_active:
                        auth_login(request,user)
                        return redirect('feed')
                else:
                        return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
             return render(request, 'login.html', context)
    
def register(request):
        if (request.method == 'POST'):
                form=UserRegistreForm(request.POST)
                if form.is_valid():
                        user = form.save(commit=False)
                        user.city_id = form.cleaned_data.get('City')
                        user.save()
                        raw_password = form.cleaned_data.get('password1')
                        raw_user=form.cleaned_data.get('username')
                        user = authenticate(username=raw_user, password=raw_password)
                        auth_login(request, user)
                        return redirect('feed')
                else:
                        print(form)
                        return redirect('register')
        else:
                partial_token = None
                if request.GET.get('partial_token'):
                        strategy = load_strategy()
                        partial_token = request.GET.get('partial_token')
                        partial = strategy.partial_load(partial_token)
                        data = partial.data['kwargs']['details']
                        form=UserRegistreForm(initial = {'username': data['username'],'email' :data['email'], 'First_name': data['first_name'],'Last_name': data['last_name']})
                        context = {'form':form}
                        return render(request, 'register.html', context)
                else:
                        form=UserRegistreForm()
                        context = {'form':form}
                        return render(request, 'register.html', context)
        
def social_auth(request):
        strategy = load_strategy()
        partial_token = request.GET.get('partial_token')
        partial = strategy.partial_load(partial_token)

        email = partial.data['kwargs']['details']['email']
        user = UserModel.objects.get(email=email)
        auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('feed')



def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)

