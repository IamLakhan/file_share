from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', show_group, name='groups'),
    path('create/', create_group),
    path('<str:pk>/delete/', delete_group),
    path('<str:pk>/add', add_person, name='add'),
    path('<str:pk>/remove', remove_person),
    path('<str:pk>/add-file', add_file),
    path('<str:pk>/remove-file', remove_file),
    path('<str:pk>/', show_one_group),
    # group home '/' => groups a user is in
    # any group  '/<str>' single group with info and messages 
    # create group '/create' 
    # delete group '/<str>delete' 
    # add memeber to group '/<str>/add'
    # remove memeber from group '/<str>/remove'
    # add files to group '/<str>/add-file'

]
