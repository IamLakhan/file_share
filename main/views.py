from django.shortcuts import render, redirect
from .models import File
# Create your views here.
def first_entry(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html',{'file': File.objects.filter(user=request.user)})
    return render(request, 'home.html')

def file_upload(request):
    if request.method == 'GET':
        return render(request, 'file-upload.html')
    if request.method == 'POST':
        user = request.user
        file_name = request.POST.get('file-name')
        upload = request.FILES['upload']
        new = File(file_name=file_name, upload=upload,user=user)
        new.save()
        return redirect('home')