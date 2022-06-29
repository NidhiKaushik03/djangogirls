from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone



def nidhi(request):
    return render(request,'blog/test.html')


# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {})


from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def Dugu(request):
    name = "Nidhi"
    classs = "MCA Pass Out"
    return render(request,'blog/dugu.html', {"name": name, "classs": classs} )