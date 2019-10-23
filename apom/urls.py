from django.urls import path
from .views import postview

urlpatterns = [
    path('', postview.post_list, name='post_list'),
]