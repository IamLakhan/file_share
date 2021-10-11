from django.shortcuts import render
from .models import File
# Create your views here.
def first_entry(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html',{'file': File.objects.filter(user=request.user)})
    return render(request, 'home.html')