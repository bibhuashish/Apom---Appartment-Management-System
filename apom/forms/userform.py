from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError

class AdminAddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'is_staff', 'password')

    def clean(self):
        cleaned_data = super(AdminAddUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

class AdminEditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser', 'is_staff')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')
