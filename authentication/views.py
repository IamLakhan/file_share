from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error':True,'message':'Please check your credentials.'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        username =email= request.POST.get('email')
        user = User.objects.filter(email=email).exists()
        if user:
            return render(request, 'register.html', {'error':True, 'message':'User already exists, try logging in.'})
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create_user(username= email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        if user:
            return redirect('login')
        return render(request, 'register.html', {'error':True,'message':'Something went wrong!'})
    return render(request, 'register.html')
