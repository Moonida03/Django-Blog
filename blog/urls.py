from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
]