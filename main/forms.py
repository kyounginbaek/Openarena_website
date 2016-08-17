from django import forms

class ContactForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput)
    phone = forms.CharField(widget=forms.TextInput)
    subject = forms.CharField(widget=forms.TextInput)
    message = forms.CharField(widget=forms.TextInput)
