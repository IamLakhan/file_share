from django.contrib import admin
from django.urls import path
from .views import login, logout, register


urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]