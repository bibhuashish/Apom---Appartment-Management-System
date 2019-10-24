from django import forms

from apom.models.pollmodel import Poll

class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ('title', 'text')