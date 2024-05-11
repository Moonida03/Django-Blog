from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import ContactForm, CommentForm
from taggit.models import Tag
from django.db.models import Count


class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status='PB')
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'list.html'


def post_list(request, tag_slug=None):
    posts = Post.objects.filter()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return render(request, 'list.html', {'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='PB')
    comments = post.comment_set.filter(active=True)
    # total_comments = post.comments.count()
    # new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', year=year, month=month, day=day, slug=slug)

    form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id) \
                        .annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags', 'published_at')[:4]

    context = {'post': post, 'comments': comments, 'form': form, 'similar_posts': similar_posts}
    return render(request, 'detail.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient_email = form.cleaned_data['recipient_email']
            comment = form.cleaned_data['comment']

            send_mail(
                "Message from {}".format(name),
                "Email: {}\n\n{}".format(email, comment),
                "from@example.com",
                [recipient_email],
                fail_silently=False,
            )
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
