from django.urls import path
from .views import postview, userview

urlpatterns = [
    path('', postview.post_list, name='post_list'),
    path('post/<int:pk>/', postview.post_detail, name='post_detail'),
    path('post/new/', postview.post_new, name='post_new'),
    path('post/<int:pk>/edit/', postview.post_edit, name='post_edit'),
    path('user/<int:pk>/', userview.user_detail, name='user_detail'),
]