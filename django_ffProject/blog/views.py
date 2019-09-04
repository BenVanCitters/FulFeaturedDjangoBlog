from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #affects list view ordering
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] #affects list view ordering
    paginate_by = 5


#override method
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
#building new with default setup
class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    #valid override
    def form_valid(self, form):
        #set the author
        form.instance.author = self.request.user
        return super().form_valid(form)

    #UserPassesTestMixin override
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    #UserPassesTestMixin override
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    #valid override
    def form_valid(self, form):
        #set the author
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request,'blog/about.html', {'title': 'about page title'})
