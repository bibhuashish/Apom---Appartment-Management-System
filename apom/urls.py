from django.urls import path
from .views import postview

urlpatterns = [
    path('', postview.post_list, name='post_list'),
    path('post/<int:pk>/', postview.post_detail, name='post_detail'),
    path('post/new/', postview.post_new, name='post_new'),
]