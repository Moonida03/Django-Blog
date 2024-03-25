from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    queryset = Post.objects.all()
    paginator = Paginator(queryset, 3)
    page_num = request.GET.get('page')
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'page': page})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, published_at__year=year,
                             published_at__month=month,
                             published_at__day=day,
                             slug=slug)
    return render(request, 'detail.html', {'post': post})