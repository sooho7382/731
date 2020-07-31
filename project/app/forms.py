from django import forms
from .models import Post, CustomUser
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','writer','image']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'grade', 'major']