from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'list.html', {'queryset': queryset})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})