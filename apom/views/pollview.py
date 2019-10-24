from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from apom.models.pollmodel import Poll
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