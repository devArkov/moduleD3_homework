from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
    queryset = None
    template_name = 'news/single.html'
    context_object_name = 'post'
