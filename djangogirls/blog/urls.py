from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('test/', views.nidhi, name = 'nidhi'),
    path('', views.post_list, name='post_list'),
    path('check/', views.Dugu, name='Dugu'),
]