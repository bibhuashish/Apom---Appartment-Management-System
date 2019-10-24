from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from apom.models.postmodel import Post
from apom.models.residentmodel import Resident
from apom.forms.postform import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context = {
        'posts': posts,
    }
    return render(request, 'apom/post_list.html', {'context': context})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    resident_authorinfo = Resident.objects.get(user=post.author.pk)
    context = {
        'post': post,
        'resident_authorinfo': resident_authorinfo,
    }
    return render(request, 'apom/post_detail.html', {'context': context})

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
    context = {
        'form': form,
        'new':1,
    }
    return render(request, 'apom/post_edit.html', {'context': context})

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
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'apom/post_edit.html', {'context': context})