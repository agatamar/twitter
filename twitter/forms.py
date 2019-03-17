from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from twitter.models import Tweet,Comment,TWITTER_MAXIMUM_COMMENT_LENGTH,Message


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'cols': 80}),
        max_length=TWITTER_MAXIMUM_COMMENT_LENGTH,
        label='')

    class Meta:
        model = Comment
        fields = ['content']
        labels = False

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content','recipient']
        widgets = {
            'content': forms.Textarea()
        }