from django.urls import path
from .views import postview, userview

urlpatterns = [
    path('', postview.post_list, name='post_list'),

    path('posts/<int:pk>/', postview.post_detail, name='post_detail'),
    path('posts/new/', postview.post_new, name='post_new'),
    path('posts/<int:pk>/edit/', postview.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete/', postview.post_edit, name='post_delete'),

    path('users/<int:pk>/', userview.user_detail, name='user_detail'),
    path('users/', userview.user_list, name='user_list'),
    path('users/<int:pk>/edit/', userview.user_edit, name='user_edit'),

    path('users/new/', userview.admin_user_new, name='user_new'),
]