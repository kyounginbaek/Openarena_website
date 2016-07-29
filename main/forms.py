from django import forms

class SignupForm(forms.Form):
    username = forms.CharField()
    nickname = forms.CharField()
    email = forms.CharField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()