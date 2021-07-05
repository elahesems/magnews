from django.shortcuts import render, get_object_or_404 ,redirect
from .models import *

# Create your views here.
def home(request):
    # siteName = 'MySite | Home'
    site = Main.objects.get(pk=2)
    context = {'site':site}
    return render(request, 'front/home.html',context)

def about(request):
    site = Main.objects.get(pk=2)
    # siteName = 'MySite | about'
    context = {'site':site}
    return render(request, 'front/about.html',context)