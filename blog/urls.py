from django.urls import path
from . import views
from .views import PostListView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from .feeds import LatestPostsFeed

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='latest_posts_feed'),
    path('search/', views.post_search, name='search')
]