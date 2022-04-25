from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Group
# Create your views here.
def show_group(request):
    user = request.user
    groups = user.group_set.all()
    context = {'groups':groups}
    return render(request, 'groups.html', context)

def show_one_group(request, pk):
    group = Group.objects.get(id=pk)
    messages = group.message_set.all()
    participants = group.participants.all()
    context = {'group':group, 'messages':messages,'participants':participants}
    return render(request, 'single-group.html', context)

def create_group(request):
    if request.method == 'POST':
        host = request.user
        name = request.POST['name']
        description = request.POST['description']
        group = Group.objects.create(host=host,name=name,description=description)
        group.participants.add(host)
        return redirect('groups')
    return render(request, 'create-group.html')

def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    return redirect('groups')

def add_person(request, pk):
    group= Group.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'add-part.html', {'message':'', 'group':group})
    email = request.POST['email']
    check = username_exists(email)
    if check:
        user = User.objects.get(username=email)
        group.participants.add(user)
        return render(request, 'add-part.html', {'message':'User added', 'group':group})
    return render(request, 'add-part.html', {'message':'User not found', 'group':group})

def username_exists(username):
    return User.objects.filter(username=username).exists()

def remove_person(request):
    pass

def add_file(request):
    pass

def remove_file(request):
    pass
