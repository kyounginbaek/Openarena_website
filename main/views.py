from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render
from django.template import Context

from main.models import Signup
from main.forms import SignupForm


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
    if request.method == 'POST':

        return HttpResponseRedirect('/')
    else:
        return render(request, 'main/login.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            tmp_username = request.POST.get("username", "")
            tmp_nickname = request.POST.get("nickname", "")
            tmp_email = request.POST.get("email", "")
            tmp_password1 = request.POST.get("password1", "")
            tmp_password2 = request.POST.get("password2", "")

            context = {
                'tmp_username': tmp_username,
                'tmp_nickname': tmp_nickname,
                'tmp_email': tmp_email,
                'tmp_password1': tmp_password1,
                'tmp_password2': tmp_password2
            }

            if tmp_password1!=tmp_password2:
                messages.error(request, "비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 한번 입력해주세요.")
                return render(request, 'main/signup.html', context)
            elif tmp_email.find(".")==-1:
                messages.error(request, "부적절한 이메일 주소입니다. 올바른 이메일 주소를 입력해주세요.")
                return render(request, 'main/signup.html')
            elif Signup.objects.filter(nickname=tmp_nickname).exists():
                messages.error(request, "이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요.")
                return render(request, 'main/signup.html')
            elif Signup.objects.filter(email=tmp_email).exists():
                messages.error(request, "이미 존재하는 이메일입니다. 다른 이메일을 입력해주세요.")
                return render(request, 'main/signup.html')

            tmp_signup = Signup(username=tmp_username, nickname=tmp_nickname, email=tmp_email,
                                password1=tmp_password1);
            tmp_signup.save()
            messages.success(request, "오픈아레나에 오신 것을 환영합니다.")
            return render(request, 'main/home.html')
    else:
        return render(request, 'main/signup.html', {})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
