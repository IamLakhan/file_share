import os
from django.shortcuts import redirect, render
from main.models import File
from .models import UserShare
from main.upload import file_upload
# Create your views here.
def share(request):
    if request.method == 'GET':
        return render(request, "share.html")
    if request.method == 'POST':
        from_user = request.user
        to_user = request.POST['to-email']
        file  = request.FILES['file']
        file_name = file.name
        file_name = file_name.replace(" ", "_")
        new = File(file_name=file_name, upload=file)
        new.save()
        new.upload = file_upload(file)
        new.save()
        user_name = from_user.first_name +' '+from_user.last_name
        sharing = UserShare(from_user=user_name, to_user=to_user, file_url=new.upload, name=file_name)
        sharing.save()
        cmd = 'uploads/'+file_name
        os.remove(cmd)
        new.delete()
        return redirect('home')
        
def shared_with_me(request): 
    user = request.user
    username = user.username
    file = UserShare.objects.filter(to_user=username)
    return render(request, 'shared-with-me.html', {"file":file})