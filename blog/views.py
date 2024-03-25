from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'list.html', {'queryset': queryset})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, published_at__year=year,
                             published_at__month=month,
                             published_at__day=day,
                             slug=slug)
    return render(request, 'detail.html', {'post': post})