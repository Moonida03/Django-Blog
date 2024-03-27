from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    recipient_email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, required=False)