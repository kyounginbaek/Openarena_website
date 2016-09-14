from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput, label="Username")
    email = forms.EmailField(widget=forms.TextInput, label="Email_address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="password (again)")

class AuthenticationForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)