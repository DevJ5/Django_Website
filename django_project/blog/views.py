from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

posts = [
    {
        'author': 'DevJ5',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Juli 18, 2020'
    },
    {
        'author': 'Mario',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Juli 19, 2020'
    }
]


def home(request):
    # context = {
    #     'posts': posts,
    # }
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
