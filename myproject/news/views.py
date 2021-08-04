from django.shortcuts import render, get_object_or_404 ,redirect
from .models import News
# Create your views here.

def new_detail(request,pk):
    news = News.objects.filter(pk=pk)
    context = {'news':news}
    return render(request, 'front/news_detail.html', context)