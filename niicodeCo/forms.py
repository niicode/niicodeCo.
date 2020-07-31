from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
    addImage = forms.ImageField()

    class Meta:
        model = Post
        fields = ('title', 'content' )



class PostCommentForm(forms.ModelForm):

    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': "form-control"}))

    class Meta:
        model = PostComment
        fields = ('comment', )

