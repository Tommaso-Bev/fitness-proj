from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")