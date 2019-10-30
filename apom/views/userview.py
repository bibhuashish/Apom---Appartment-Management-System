from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from apom.models.pollmodel import Poll
from apom.models.residentmodel import Resident
from apom.models.postmodel import Post
from apom.forms.userform import UserForm, AdminAddUserForm, AdminEditUserForm
from apom.forms.residentform import ResidentForm, AdminResidentForm
from django.shortcuts import redirect


def user_list(request):
    usersinfo = User.objects.filter().order_by('-is_superuser')
    extrainfo = []
    for userinfo in usersinfo:
        extrainfo.append(Resident.objects.get(user=userinfo.pk))
    usersinfo = zip(usersinfo, extrainfo)
    context = {
        'usersinfo': usersinfo,
    }
    return render(request, 'apom/user_list.html', {'context' : context})

def user_detail(request, pk):
    userinfo = get_object_or_404(User, pk=pk)
    residentinfo = Resident.objects.get(user=pk)
    posts = Post.objects.filter(author=userinfo,published_date__lte=timezone.now()).order_by('-published_date')[:5]
    # polls = Poll.objects.filter(author=userinfo, published_date__lte=timezone.now()).order_by('-published_date')[:5]
    context = {
        'userinfo': userinfo,
        'residentinfo': residentinfo,
        'posts': posts,
        # 'polls': polls
    }
    return render(request, 'apom/user_detail.html', {'context': context})

def admin_user_new(request):
    if request.method == "POST":
        userform = AdminAddUserForm(request.POST)
        residentform = AdminResidentForm(request.POST)
        if userform.is_valid() and residentform.is_valid():
            user = userform.save(commit=False)
            resident = residentform.save(commit=False)
            user.set_password(user.password)
            user.date_joined = timezone.now()
            user.save()
            resident.user = user
            resident.save()
            return redirect('user_detail', pk=user.pk)
    else:
        userform = AdminAddUserForm()
        residentform = AdminResidentForm()
    context = {
        'userform': userform,
        'residentform': residentform,
        'new':1,
    }
    return render(request, 'apom/user_edit.html', {'context': context})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    resident = get_object_or_404(Resident, user=pk)
    if request.method == "POST":
        if(request.user.is_superuser):
            userform = AdminEditUserForm(request.POST, instance=user)
            residentform = AdminResidentForm(request.POST, instance=resident)
        else:
            userform = UserForm(request.POST, instance=user)
            residentform = ResidentForm(request.POST, instance=resident)
        if userform.is_valid() and residentform.is_valid():
            user = userform.save(commit=False)
            resident = residentform.save(commit=False)
            user.save()
            resident.save()
            return redirect('user_detail', pk=user.pk)
    else:
        if (request.user.is_superuser):
            userform = AdminEditUserForm(instance=user)
            residentform = AdminResidentForm(instance=resident)
        else:
            userform = UserForm(instance=user)
            residentform = ResidentForm(instance=resident)
    context = {
        'userform': userform,
        'residentform': residentform,
        'userinfo': user,
    }
    return render(request, 'apom/user_edit.html', {'context': context})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if(request.user.is_superuser):
        user.delete()
    return redirect('user_list')
