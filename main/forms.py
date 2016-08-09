from django import forms

class SignupForm(forms.Form):
    username = forms.CharField()
    nickname = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class LoginForm(forms.Form):
    email = forms.CharField()
    password1 = forms.CharField()

class MakingForm(forms.Form):
    name = forms.CharField()
