from django.contrib import admin
from django.urls import path, include
from .views import file_upload, first_entry

urlpatterns = [
    path('file-upload/', file_upload, name="upload"),
    # path('', first_entry, name = 'home'),
]
