from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def fixtures(request):
    return render(request,'common/fixtures.html')

def madridistas(request):
    return render(request,'common/madridistas.html')

def players(request):
    return render(request,'common/players.html')

def stores(request):
    return render(request,'common/stores.html')            