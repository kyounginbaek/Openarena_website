import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from accounts.forms import RegistrationForm, AuthenticationForm
from main.models import Tournament, Funding, Fundingdummy, Participation

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            tmp_username = request.POST.get('username')
            tmp_email = request.POST.get('email')
            tmp_password1 = request.POST.get('password1')
            tmp_password2 = request.POST.get('password2')

            if tmp_password1 != tmp_password2:
                response = {'status':'fail', 'message': "비밀번호와 비밀번호 확인이 일치하지 않습니다. 다시 한번 확인해주세요."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif tmp_email.find(".") == -1:
                response = {'status':'fail', 'message': "부적절한 이메일 주소입니다. 올바른 이메일 주소를 입력해주세요."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif User.objects.filter(username=tmp_username).exists():
                response = {'status':'fail', 'message': "이미 존재하는 닉네임입니다. 다른 닉네임을 입력해주세요."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            elif User.objects.filter(email=tmp_email).exists():
                response = {'status':'fail', 'message': "이미 존재하는 이메일입니다. 다른 이메일을 입력해주세요."}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                user = User.objects.create_user(
                    username=tmp_username,
                    password=tmp_password1,
                    email=tmp_email
                )

                user = authenticate(username=tmp_email, password=tmp_password1)
                auth_login(request, user)
                response = {'status': 'success', 'message': "로그인 성공."}
                return HttpResponse(json.dumps(response), content_type='application/json')
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            tmp_email = request.POST.get('email')
            tmp_password = request.POST.get('password')

            user = authenticate(username=tmp_email, password=tmp_password)

            if user is not None:
                auth_login(request, user)
                data = {'status': 'success', 'message': "로그인 성공."}
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = {'status':'fail', 'message': "아이디 및 비밀번호가 일치하지 않습니다. 다시 한번 확인해주세요."}
                return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return render(request, 'accounts/login.html', {})

def logout(request):
    auth_logout(request)
    return redirect('/')

def mypage(request):
    if not request.user.is_authenticated():
        messages.success(request, "로그인이 필요한 페이지입니다. 먼저 로그인을 해주세요.")
        return render(request, 'accounts/login.html', {})
    else:
        # 초기화
        participation_info = 0
        funding_info = 0
        tournament_info = 0

        # 참가한 대회가 있는지 여부
        if Participation.objects.filter(username=request.user.username).exists():
            participation_info = Participation.objects.filter(username=request.user.username)
        if Funding.objects.filter(username=request.user.username).exists():
            funding_info = Funding.objects.filter(username=request.user.username)
        if Tournament.objects.filter(username=request.user.username).exists():
            tournament_info = Tournament.objects.filter(username=request.user.username)

        return render(request, 'accounts/mypage.html', {'participation_info': participation_info,
                                                        'funding_info': funding_info,
                                                        'tournament_info': tournament_info})

def withdrawal(request):
    # 회원탈퇴 시 비밀번호 변경

    return redirect('/')
