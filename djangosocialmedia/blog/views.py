from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView
    )

# Create your views here.

# The following is a function based view 
def home(request):
    
    context = {
        "posts":Post.objects.all(),
        "title": 'Home'
    }
    return render(request, "blog/home.html", context)

# The following is a class based ListView 
class PostListView(ListView):
    model = Post 
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.User
        return super().form_valid(form)




def about(request):
    return render(request, "blog/about.html")

