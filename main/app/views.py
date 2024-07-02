from django.shortcuts import render,redirect
from .models import Video
# Create your views here.
def home(request):
    videos=Video.objects.all()
    return render (request,'home.html',{'videos':videos})
def upload(request):
    if request.method=='POST':
        name=request.POST['name']
        video=request.FILES.get('video')
        var=Video.objects.create(name=name,video=video)
        var.save()
        return redirect('home')
    return render(request,'upload.html')
def download(request,video_id):
    return render(request,'download.html')