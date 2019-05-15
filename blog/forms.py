from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter description here'})
        }
