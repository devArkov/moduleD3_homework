from django.views.generic import ListView, DetailView

from .models import Post


class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-created_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SingleNewsView(DetailView):
    model = Post
    template_name = 'news/single.html'
    context_object_name = 'post'

