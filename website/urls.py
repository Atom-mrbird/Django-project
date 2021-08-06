"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from project.views import starting_page, joke_page, create_page, jokelist,JokeDetailView,connect_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', starting_page, name="index"),
    path('gallery', joke_page, name="jokes"),
    path('create', create_page, name="create"),
    path('api', jokelist.as_view(), name="list"),
    path('api/<id>/', JokeDetailView.as_view(), name="del"),
    path('connect', connect_api, name='connect')
]
