from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from apom.models.postmodel import Post
from apom.models.residentmodel import Resident
from apom.forms.postform import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    currentuser = request.user
    return render(request, 'apom/post_list.html', {'posts': posts, 'user' : currentuser})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    authorinfo = Resident.objects.get(user=post.author.pk)
    return render(request, 'apom/post_detail.html', {'post': post, 'authorinfo': authorinfo})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'apom/post_edit.html', {'form': form, 'new':1})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'apom/post_edit.html', {'form': form, 'post': post})