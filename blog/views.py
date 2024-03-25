from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status='PB')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, published_at__year=year,
                             published_at__month=month,
                             published_at__day=day,
                             slug=slug)
    return render(request, 'detail.html', {'post': post})