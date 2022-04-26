import os
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main.models import File

from main.upload import file_upload
from .models import Group, Message
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def show_group(request):
    user = request.user
    groups = user.group_set.all()
    context = {'groups':groups}
    return render(request, 'groups.html', context)

@login_required(login_url='login')
def show_one_group(request, pk):
    group = Group.objects.get(id=pk)
    messages = group.message_set.all()
    participants = group.participants.all()
    admin = False
    if(request.user == group.host): admin = True
    context = {'group':group, 'messages':messages,'participants':participants, 'admin':admin}
    return render(request, 'single-group.html', context)

@login_required(login_url='login')
def create_group(request):
    if request.method == 'POST':
        host = request.user
        name = request.POST['name']
        description = request.POST['description']
        group = Group.objects.create(host=host,name=name,description=description)
        group.participants.add(host)
        return redirect('groups')
    return render(request, 'create-group.html')

@login_required(login_url='login')
def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    if group.host != request.user:
        return HttpResponse('You are not allowed to do this')
    group.delete()
    return redirect('groups')

@login_required(login_url='login')
def add_person(request, pk):
    group= Group.objects.get(id=pk)
    if group.host != request.user:
        return HttpResponse('You are not allowed to do this')
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
@login_required(login_url='login')
def remove_person(request, pk, rp):
    if request.method=='GET':
        user = request.user
        group = Group.objects.get(id=pk)
        if group.host != user:
            return HttpResponse('You are not allowed to do this')
        user2 = User.objects.get(id=rp)
        group.participants.remove(user2)
        return redirect(request.META.get('HTTP_REFERER'))
        
@login_required(login_url='login')
def add_file(request,pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, 'add-file.html', {'group': group})
    user = request.user
    # group = Group.objects.get(id=pk)
    if group.host != user:
        return HttpResponse('You are not allowed to do this')
    file  = request.FILES['file']
    name = file.name
    name = name.replace(" ", "_")
    new = File(file_name=name, upload=file)
    new.save()
    new.upload = file_upload(file)
    new.save()
    message = Message(user=user, group=group,name=name,file_url=new.upload)
    message.save()
    cmd = 'uploads/'+name
    os.remove(cmd)
    new.delete()
    path = request.META.get('HTTP_REFERER')
    return redirect(path[0:-9])

@login_required(login_url='login')
def remove_file(request, pk, fid):
    if request.method=='GET':
        user = request.user
        group = Group.objects.get(id=pk)
        if group.host != user:
            return HttpResponse('You are not allowed to do this')
        message = Message.objects.get(id=fid)
        message.delete()
        return redirect(request.META.get('HTTP_REFERER'))
