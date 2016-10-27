import json
import random
import requests
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Making, Funding


def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    if not request.user.is_authenticated():
        messages.success(request, "준비중인 기능입니다.")
        return render(request, 'main/home.html', {})

    if request.method == 'POST':
        # 토너먼트 URL 체크
        tournament_url = request.POST.get('tournament_url')
        if Making.objects.filter(tournament_url=tournament_url).exists():
            response1 = {'status': 'error'}
            return HttpResponse(json.dumps(response1), content_type='application/json')

        # 스트리밍 URL (afreecatv or twitch)
        streaming_url_spec = request.POST.get('input_afreecatv')+request.POST.get('input_twitch')+\
                             request.POST.get('input_youtube')+request.POST.get('input_facebook')

        # 체크인 기능 NULL 방지
        if request.POST.get('checkin') is not None:
            checkin = request.POST.get('checkin')
        else:
            checkin = "no"

        # 참가자명/팀명(필수), 참가자 연락처, 참가자 이메일, 추가 필요양식(input)
        template = "name"
        if request.POST.get('template_phone') is not None:
            template += ".phone"
        if request.POST.get('template_email') is not None:
            template += ".email"
        if request.POST.get('input_template_etc') is not None:
            template += "." + str(request.POST.get('input_template_etc'))

        # save 코드
        making_obj = Making(username=request.user.username, email=request.user.email, tournament_name=request.POST.get('tournament_name'),
                                tournament_game=request.POST.get('tournament_game'), tournament_url = request.POST.get('tournament_url'),
                                streaming_url=request.POST.get('streaming_url'), streaming_url_spec=streaming_url_spec,
                                registration=request.POST.get('registration'), registration_team=request.POST.get('registration_team'),
                                participant=request.POST.get('participant'), starttime=request.POST.get('starttime'), funding_goal=request.POST.get('funding_goal'),
                                checkin=checkin, checkin_time=request.POST.get('checkin_time'), description=request.POST.get('description'),
                                promise=request.POST.getlist('promise[]'), promise_spec= request.POST.getlist('promise_spec[]'), reward=request.POST.getlist('reward[]'), reward_spec=request.POST.getlist('reward_spec[]'),
                                template=template, phone=request.POST.get('phone'))
        making_obj.save()
        response2 = {'status': 'success',
                    'message': "대회 생성 요청이 성공적으로 제출되었습니다. 빠른 시일 내에 운영진과 검토 후 이메일과 연락처로 대회 개최 여부를 말씀드리겠습니다."}
        return HttpResponse(json.dumps(response2), content_type='application/json')

    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def contents(request):
    return render(request, 'main/contents.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def competition(request):
    return render(request, 'main/competition.html', {})

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        emailsend = EmailMessage("보낸사람: "+email+" / "+"제목: "+subject, "내용: "+message+"\n"+"연락처: "+phone, to=['help@openarena.kr'])
        emailsend.send()

        response = {'status': 'success',
                    'message': "문의가 정상적으로 접수되었습니다. 빠른 시일 내에 답변드리도록 하겠습니다."}
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'main/contact.html', {})

def help(request):
    return render(request, 'main/help.html', {})

def funding(request):
    if request.method == 'POST':
        funding_amount = request.POST.get('funding_amount')

        url = "https://toss.im/tosspay/api/v1/payments"
        params = {
            "orderNo": "2016091901"+str(random.randrange(1,99999999)),
            "amount": funding_amount,
            "productDesc": "미갈리스의 하스스톤 대회",
            "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
            "expiredTime": "2015-09-19 19:00:00",
        }

        response = requests.post(url, data=params)
        #print(response.text)

        if response.json().get('status') == 200 and response.json().get('code') != -1:
            # save 코드
            funding_obj = Funding(username=request.user.username, email=request.user.email,
                                  orderno=params.get('orderNo'), amount=params.get('amount'))
            funding_obj.save()
            return redirect(response.json().get('checkoutPage'))
        else:
            response = {'status': 'fail'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'main/competition.html', {})

def privacy(request):
    return render(request, 'main/privacy.html', {})

def agreement(request):
    return render(request, 'main/agreement.html', {})
