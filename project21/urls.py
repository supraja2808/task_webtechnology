"""
URL configuration for project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('h1/',h1,name='h1'),
    path('h2/',h2,name='h2'),
    path('h3/',h3,name='h3'),
    path('h4/',h4,name='h4'),
    path('h5/',h5,name='h5'),
    path('h6/',h6,name='h6'),
    path('h7/',h7,name='h7'),
    path('h8/',h8,name='h8'),
    path('h9/',h9,name='h9'),
    path('h10/',h10,name='h10'),
    path('h11/',h11,name='h11'),
    path('h12/',h12,name='h12'),
    path('h13/',h13,name='h13'),
    path('h14/',h14,name='h14'),
    path('h15/',h15,name='h15'),
    path('h16/',h16,name='h16'),
    path('h17/',h17,name='h17'),
    path('h18/',h18,name='h18'),
    path('h19/',h19,name='h19'),
    path('h20/',h20,name='h20'),
    path('h21/',h21,name='h21'),


      
     


]

