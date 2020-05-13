from django.shortcuts import render
from deriveweb.models import DeriveHome, DeriveBeer
# Create your views here.


def derive_home(request):
    derivehome = DeriveHome.objects.all()
    return render(request, 'index.html',
                  {'derivehome': derivehome})


def derive_beer(request):
    derivebeer = DeriveBeer.objects.all()
    return render(request, 'beer.html',
                  {'derivebeer': derivebeer})