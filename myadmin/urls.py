"""
URL configuration for Ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myadmin import views
from .views import *


urlpatterns = [
    path('index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_category', views.add_category, name='add_category'),
    path('all_category', views.all_category, name='all_category'),
    path('add_product', views.add_product, name='add_product'),
]
