from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .forms import ContactForm


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