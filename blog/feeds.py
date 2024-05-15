from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    title = "Latest Posts"
    link = reverse_lazy('post_list')
    description = "Latest Posts on Blog"

    def items(self):
        return Post.published.order_by('-published_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body