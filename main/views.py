from django.contrib import messages
from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    if not request.user.is_authenticated():
        messages.success(request, "로그인이 필요한 페이지입니다. 먼저 로그인을 해주세요.")
        return render(request, 'accounts/login.html', {})
    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def competition(request):
    return render(request, 'main/competition.html', {})

def contact(request):
    return render(request, 'main/contact.html', {})

def help(request):
    return render(request, 'main/help.html', {})
