
from django import forms
from django.contrib.auth.models import User
from .models import UserInfo


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('date_of_birth',)
