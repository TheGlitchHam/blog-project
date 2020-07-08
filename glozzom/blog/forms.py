from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {'author': forms.Select(),
                   'title': forms.TextInput(attrs={'class': 'textinputclass'}),
                   'text': forms.Textarea(attrs={'id': 'editor1', 'class': 'editable medium-editor-textarea postcontent', 'name': 'custom_editor'})}


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'id': 'editor1', 'class': 'editable medium-editor-textarea', 'name': 'custom_editor'})

        }
