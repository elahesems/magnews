from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('news/<str:pk>/', views.new_detail, name='news_detail'),


]