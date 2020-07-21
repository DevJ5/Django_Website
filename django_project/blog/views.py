from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
# from django.http import HttpResponse

# posts = [
#     {
#         'author': 'Luigi',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date_posted': 'Juli 18, 2020'
#     },
#     {
#         'author': 'Mario',
#         'title': 'Blog post 2',
#         'content': 'Second post content',
#         'date_posted': 'Juli 19, 2020'
#     }
# ]


# Function based view that uses either in memory dictionary or objects from the DB
# def home(request):
#     # context = {
#     #     'posts': posts,
#     # }
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

# Class based view that makes use of a list view
class PostListView(ListView):
    model = Post
    # template name is used because Django will use a different path
    template_name = 'blog/home.html'
    # context object name is used because Django will pass Objectlist down to template
    context_object_name = 'posts'
    # use minus sign to order DESC
    ordering = ['-date_posted']
    paginate_by = 5


# Get all posts by a certain user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # get the username from the url
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overwrite the parent form_valid function to set the User FK
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overwrite the parent form_valid function to set the User FK
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
