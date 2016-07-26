from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from main.forms import RegistrationForm

# main view
def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def login(request):
    return render(request, 'main/login.html', {})

# signup, login, logout
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                nickname=form.cleaned_data['nickname'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        '/login.html',
        variables,
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
