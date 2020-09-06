"""Hire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from .views import (index, register, levels, level1,level2,level3,level4,level5,level6,level7,level8,level9, level10,ins)
urlpatterns = [
    path('', index, name='index'),
    path('register/', register),
    path('levels/', levels),
    path('instructions/',ins),
    path('level1/', level1, name='level1'),
    path('level2/', level2, name='level2'),
    path('level3/', level3, name='level3'),
    path('level4/', level4, name='level4'),
    path('level5/', level5, name='level5'),
    path('level6/', level6, name='level6'),
    path('level7/', level7, name='level7'),
    path('level8/', level8, name='level8'),
    path('level9/', level9, name='level9'),
    path('level10/', level10, name='level10'),
]
