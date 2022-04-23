from django.contrib import admin
from django.urls import path, include
from .views import share, shared_with_me

urlpatterns = [
    path('share/', share),
    path('shared-with-me/', shared_with_me)
]
