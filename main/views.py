from django.shortcuts import render, redirect
from .models import File
import requests
from .secrets import jwt
import os
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
        url = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
        files = {'file': open(str(new.upload), 'rb')}
        header = {'Authorization': 'Bearer {}'.format(jwt)}
        my_response = requests.post(url, headers=header, files=files)
        hash_value = my_response.text[13:59]
        upload_url = 'ipfs.io/ipfs/' + hash_value
        cmd = 'rm {}'.format(new.upload)
        os.system(cmd)
        new.upload = upload_url
        new.save()
        return redirect('home')

        