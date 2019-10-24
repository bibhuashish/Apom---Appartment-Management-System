from django import forms

from apom.models.residentmodel import Resident

class AdminResidentForm(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ('role', 'community', 'block', 'home')

class ResidentForm(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ('community', 'block', 'home')