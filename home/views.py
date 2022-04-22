from django.shortcuts import get_object_or_404, render
from .models import Work_Samples

# Create your views here.

def home(request):
    work_samples = Work_Samples.objects.filter(status=True)
    context = {
        "work":work_samples,
    }
    return render(request, 'all/home.html',context)

def about(request):
    return render(request,'all/about.html')

def contact(request):
    return render(request,'all/contact.html')



def detail(request, slug):
    post = get_object_or_404(Work_Samples , slug=slug ,status=True)
    context = {
        'post':post
    }
    return render(request,'all/posts.html')