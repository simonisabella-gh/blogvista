from django import forms
from .models import Post,Comment

class CommentForm(forms.ModelForm):
    # author = forms.CharField(
    #     max_length=60,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Your Name"}
    #     ),
    # )
    # body = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"class": "form-control", "placeholder": "Leave a comment!"}
    #     )
    # )
    class Meta:
        model=Comment
        fields=['post','body','author','created_on']
        exclude=['author','post','created_on']


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','post_img','body','author','created_on','last_modified','categories']
        exclude=['author','created_on','last_modified',]






