from django.shortcuts import render, get_object_or_404 ,redirect
from .models import *

# Create your views here.
def home(request):
    siteName = 'MySite | Home'
    context = {'siteName':siteName}
    return render(request, 'front/home.html',context)

def about(request):
    siteName = 'MySite | about'
    context = {'siteName':siteName}
    return render(request, 'front/about.html',context)