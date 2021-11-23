from django.contrib import admin
from django.urls import path
from .views import login_user, logout_user, register


urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user),
    path('register/', register, name="register"),
]