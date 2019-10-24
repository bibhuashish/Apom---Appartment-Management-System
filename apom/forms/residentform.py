from django import forms

from apom.models.residentmodel import Resident

ROLES = [
    ('Owner', 'Owner'),
    ('Tenant', 'Tenant'),
    ('Maintenance Staff', 'Maintenance Staff'),
]

class AdminResidentForm(forms.ModelForm):
    role = forms.CharField(widget=forms.Select(choices=ROLES))
    class Meta:
        model = Resident
        fields = ('role', 'community', 'block', 'home')

class ResidentForm(forms.ModelForm):

    class Meta:
        model = Resident
        fields = ('community', 'block', 'home')