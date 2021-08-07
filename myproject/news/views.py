from django.shortcuts import render, get_object_or_404 ,redirect
from main.models import Main
from .models import News
# Create your views here.

def new_detail(request,pk):
    site = Main.objects.get(pk=3)
    news = News.objects.filter(pk=pk)
    context = {'site':site, 'news':news}
    return render(request, 'front/news_detail.html', context)
