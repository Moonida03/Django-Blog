from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
]