from django.contrib import admin
from django.urls import path, include
from .views import file_upload, first_entry, file_delete

urlpatterns = [
    path('file-upload/', file_upload, name="upload"),
    path('file-delete/<int:fid>', file_delete, name='delete')
    # path('', first_entry, name = 'home'),
]
