from django import forms
from .models import Comment

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    recipient_email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField()