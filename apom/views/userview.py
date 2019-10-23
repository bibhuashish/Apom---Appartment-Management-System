from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from apom.models.residentmodel import Resident
from apom.models.postmodel import Post

def user_list(request):
    usersinfo = User.objects.filter().order_by('-is_superuser')
    extrainfo = []
    for userinfo in usersinfo:
        extrainfo.append(Resident.objects.get(user=userinfo.pk))
    usersinfo = zip(usersinfo, extrainfo)
    return render(request, 'apom/user_list.html', {'usersinfo': usersinfo})

def user_detail(request, pk):
    userinfo1 = get_object_or_404(User, pk=pk)
    userinfo2 = Resident.objects.get(user=pk)
    posts = Post.objects.filter(author=userinfo1,published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'apom/user_detail.html', {'userinfo1': userinfo1, 'userinfo2': userinfo2, 'posts': posts})
