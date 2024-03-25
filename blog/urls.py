from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
]