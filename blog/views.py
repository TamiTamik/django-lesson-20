from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.
def index(request):
    return render(request, 'index.html')
def post(request):
    posts = Post.objects.all()
    data = {
        'posts':posts
    }
    return render(request, 'post.html', data)
def comment(request):
    return render(request, 'comment.html')
def about(request):
    return render(request, 'about.html')