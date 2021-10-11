from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def first_entry(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html',{'user': User.objects.get(username=request.user.username)})
    return render(request, 'home.html')