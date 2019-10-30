from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from apom.models.pollmodel import Poll
from apom.models.pollrecordmodel import Pollrecord
from apom.models.residentmodel import Resident
from apom.forms.pollform import PollForm
from django.shortcuts import redirect

def poll_list(request):
    polls = Poll.objects.order_by('-published_date')
    context = {
        'polls': polls,
    }
    return render(request, 'apom/poll_list.html', {'context': context})

def poll_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    resident_authorinfo = Resident.objects.get(user=poll.author.pk)
    context = {
        'poll': poll,
        'resident_authorinfo': resident_authorinfo,
    }
    return render(request, 'apom/poll_detail.html', {'context': context})


def poll_new(request):
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.author = request.user
            poll.published_date = timezone.now()
            poll.save()
            return redirect('poll_detail', pk=poll.pk)
    else:
        form = PollForm()
    context = {
        'form': form,
        'new':1,
    }
    return render(request, 'apom/poll_edit.html', {'context': context})

def poll_edit(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if request.method == "POST":
        form = PollForm(request.POST, instance=poll)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.author = request.user
            poll.published_date = timezone.now()
            poll.save()
            return redirect('poll_detail', pk=poll.pk)
    else:
        form = PollForm(instance=poll)
    context = {
        'form': form,
        'poll': poll,
    }
    return render(request, 'apom/poll_edit.html', {'context': context})

def poll_delete(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    if(poll.author.id == request.user.pk):
        poll.delete()
    return redirect('user_detail', pk=poll.author.pk)

def poll_like(request, pk):
    user = request.user
    if user.is_authenticated:
        poll = Poll.objects.filter(pk=pk).first()
        if (poll):
            pollrecord = Pollrecord.objects.filter(user=user.pk, poll=pk).first()
            if (pollrecord and not pollrecord.choice):
                poll.negative -= 1
                pollrecord.choice = True
                poll.positive += 1
                pollrecord.save()
            elif not pollrecord:
                Pollrecord.objects.create(user=user, poll=poll, choice=True)
                poll.positive += 1
            poll.save()
    return redirect('poll_detail', pk=pk)

def poll_dislike(request, pk):
    user = request.user
    if user.is_authenticated:
        poll = Poll.objects.filter(pk=pk).first()
        if (poll):
            pollrecord = Pollrecord.objects.filter(user=user.pk, poll=pk).first()
            if (pollrecord and pollrecord.choice):
                poll.positive -= 1
                pollrecord.choice = False
                poll.negative += 1
                pollrecord.save()
            elif not pollrecord:
                Pollrecord.objects.create(user=user, poll=poll, choice=False)
                poll.negative += 1
            poll.save()
    return redirect('poll_detail', pk=pk)