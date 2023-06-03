from django.shortcuts import render
from .models import Post
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def index(request):
    features = Post.objects.all()
    return render(request, 'index.html', {'features' : features})

def home(request):
    if request.method == 'POST':
        img = request.POST.get('imgs')
        addr = request.POST['address']
        time = datetime.now()
        new_Post = Post(image=img, address = addr, dated = time)
        new_Post.save()
    return render(request, 'home.html')

def notify(request):
    features = Post.objects.all()
    return render(request, 'notification.html', {'features' : features})

def guide(request):
    return render(request, 'guide.html')
