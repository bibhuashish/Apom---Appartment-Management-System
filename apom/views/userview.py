from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from apom.models.residentmodel import Resident
from apom.models.postmodel import Post
from apom.forms.postform import PostForm
from django.shortcuts import redirect

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     currentuser = request.user
#     return render(request, 'apom/post_list.html', {'posts': posts, 'user' : currentuser})

def user_detail(request, pk):
    userinfo1 = get_object_or_404(User, pk=pk)
    userinfo2 = Resident.objects.get(user=pk)
    posts = Post.objects.filter(author=userinfo1,published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'apom/user_detail.html', {'userinfo1': userinfo1, 'userinfo2': userinfo2, 'posts': posts})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'apom/post_edit.html', {'form': form, 'new':1})
#
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     currentuser = request.user
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'apom/post_edit.html', {'form': form, 'post': post, 'user': currentuser})