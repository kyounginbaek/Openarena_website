import json
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from main.models import Signup
from main.forms import SignupForm, LoginForm

# main view
def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    if not request.user.is_authenticated():
        return redirect('login')
    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def competition(request):
    return render(request, 'main/competition.html', {})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            tmp_email = request.POST.get("email", "")
            tmp_password1 = request.POST.get("password1", "")

            if Signup.objects.filter(email=tmp_email).exists():
                if Signup.objects.get(email=tmp_email).password1==tmp_password1:
                    tmp_nickname = Signup.objects.get(email=tmp_email).nickname
                    context = {
                        'tmp_nickname': tmp_nickname,
                        'tmp_email': tmp_email,
                        'status_login' : "로그아웃"
                    }
                    return render(request, 'main/home.html', context)
                else:
                    data = {'message': "비밀번호가 일치하지 않습니다. 다시 한번 확인해주세요."}
                    return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {'message': "아이디가 존재하지 않습니다. 신규 방문자는 회원가입을 해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return render(request, 'main/login.html', {})

def mypage(request):
    return render(request, 'main/mypage.html', {})

def support(request):
    return render(request, 'main/support.html', {})

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
                'tmp_nickname': tmp_nickname,
                'tmp_email': tmp_email,
                'status_login' : "로그아웃"
            }

            if tmp_password1!=tmp_password2:
                data = {'message': "비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 한번 확인해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')
            elif tmp_email.find(".")==-1:
                data = {'message': "부적절한 이메일 주소입니다. 올바른 이메일 주소를 입력해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')
            elif Signup.objects.filter(nickname=tmp_nickname).exists():
                data = {'message': "이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')
            elif Signup.objects.filter(email=tmp_email).exists():
                data = {'message': "이미 존재하는 이메일입니다. 다른 이메일을 입력해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')

            tmp_signup = Signup(username=tmp_username, nickname=tmp_nickname, email=tmp_email,
                                password1=tmp_password1);
            tmp_signup.save()
            return render(request, 'main/home.html', context)
    else:
        return redirect('home')

def logout(request):
    return redirect('home')

def help(request):
    return render(request, 'main/help.html', {})
