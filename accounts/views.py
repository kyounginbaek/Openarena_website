from django.contrib import messages
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout

from accounts.forms import AuthenticationForm, RegistrationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    return redirect('/')
    else:
        return render(request, 'accounts/login.html', {})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        return redirect('login')

def logout(request):
    django_logout(request)
    return redirect('/')

def mypage(request):
    #if not request.user.is_authenticated():
    #    messages.success(request, "로그인이 필요한 페이지입니다. 먼저 로그인을 해주세요.")
    #    return render(request, 'accounts/login.html', {})
    return render(request, 'accounts/mypage.html', {})