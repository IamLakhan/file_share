from django.shortcuts import render, redirect
from .models import File
import os
from .upload import file_upload as fileto_upload
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
        upload  = request.FILES['upload']
        file_name = upload.name
        file_name = file_name.replace(" ", "_")
        new = File(file_name=file_name, upload=upload,user=user)
        new.save()
        new.upload = fileto_upload(upload)
        new.save()
        cmd = 'uploads/'+file_name
        os.remove(cmd)
        return redirect('home')

def file_delete(request, fid):
    if fid:
        File.objects.filter(id=fid).delete()
    return redirect('home')
        