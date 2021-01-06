from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)


# A little something about class-based views:

# At its core, a class-based view allows you to respond to different HTTP request methods with different class instance methods, 
# instead of with conditionally branching code inside a single view function.

# Attributes associated with class-based views can be overridden either by either one of the following methods:
# 1. Passing in the name of the attribute and its value within the as_view() method, such as like template_name = "bhains.html"
# 2. Or you can do what we have done below, and simply associating a value for a particular attribute 

# Create your views here.

# The following is a function based view and is not being used since its corresponding urls pattern has been commented out. 
def home(request):

    context = {
        "posts":Post.objects.all(),
        "title": 'Home'
    }
    return render(request, "blog/home.html", context)

# The following is a class based ListView 
class PostListView(LoginRequiredMixin, ListView):

    model = Post 
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post 
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')
        

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # success_url = This attribute is to be used to redirect to the home page upon the successful creation of a post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            False




def about(request):
    return render(request, "blog/about.html")

