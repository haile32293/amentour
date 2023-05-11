from django.shortcuts import render
from .models import *

# Create your views here.

def domestic(request):
    return render (request, "base.html", {})

def about(request):
    return render(request, 'about.html', {})

def index(request):
    return render(request, "index.html", {})

def booking(request):
    return render(request, 'booking',{})

def contact(request):
    return render(request, 'contact.html', {})
def service(request):
    return render(request, 'service.html', {})
def packages(request):
    package = Package.objects.all()
    return render(request, 'package.html', {'packages':package})


def destinations(request):
    return render(request, 'destination.html', {})
