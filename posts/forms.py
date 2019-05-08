from django import forms
from django.contrib.auth.models import User
from login.models import UserProfileInfo
from posts.models import post

class PostForm(forms.ModelForm):
    # password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = post
        fields = ('title','description')

