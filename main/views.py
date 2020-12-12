from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Registration
from django.http import JsonResponse
import datetime
import requests
import json

# Create your views here.
def index(request):
    name = ""
    username = ""
    date = datetime.datetime.now().hour
    text = "test"
    if date < 11 and date >= 3:
        text = "Good Morning"
    elif date >= 11 and date < 15:
        text = "Good Afternoon"
    elif date >= 15 and date < 18:
        text = "Good Evening"
    elif date >= 18 or date < 3:
        text = "Good Night"

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            name = request.user.first_name + " " + request.user.last_name
        else :
            messages.error(request,'username or password is not correct')
    context = {'text':text, 'name':name, 'username':username}
    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else :
        form = Registration()
    return render(request, 'register.html', {'form' : form})

def logOut(request):
    logout(request)
    return redirect('/')

def data(request):
    url = "https://www.googleapis.com/books/v1/volumes?q=" + request.GET['q']
    ret = requests.get(url)
    data = json.loads(ret.content)
    return JsonResponse(data, safe=False)