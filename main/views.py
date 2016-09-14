import json
import random

import requests
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Tournament, Funding


def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def tournament_url_check(request):
    if request.method == 'POST':
        tournament_url = request.POST.get('tournament_url')
        if Tournament.objects.filter(tournament_url=tournament_url).exists():
            response = {'status': 'error', 'message': "이미 존재하는 대회 url입니다."}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            response = {'status': 'success', 'message': "존재하지 않는 적절한 url입니다."}
            return HttpResponse(json.dumps(response), content_type='application/json')

def making(request):
    if not request.user.is_authenticated():
        messages.success(request, "준비중인 기능입니다.")
        return render(request, 'main/home.html', {})

    if request.method == 'POST':
        # 스트리밍 URL (afreecatv or twitch)
        streaming_url_spec = request.POST.get('input_afreecatv')+request.POST.get('input_twitch')

        # 단일 방식 토너먼트(single_tournament) & 혼합 방식 토너먼트(two_tournament)
        tournament_type = request.POST.get('tournament_type')

        # 싱글 엘리미네이션(single_elimination_final) & 더블 엘리미네이션(double_elimination_final) & 라운드 로빈(round_robin_final) & 스위스리그(swiss_final)
        tournament_format = request.POST.get('single_tournament_final')+request.POST.get('two_tournament_group')+"."+request.POST.get('two_tournament_final')

        # 싱글 엘리미네이션 -> 3위 결정전
        # 더블 엘리미네이션 -> 1-2경기, 1경기, 없음
        # 라운드 로빈 -> 등급순위(), 등급순위 -> custom_points 4개 항목
        # 스위스리그 -> 5개 항목 값
        if tournament_type == "single_tournament":
            tournament_spec = request.POST.get('single_elimination_final_spec')+request.POST.get('double_elimination_final_spec')\
                              +request.POST.get('round_robin_final_spec')+"."+request.POST.get('custom_points_system_final_spec1')+"."+request.POST.get('custom_points_system_final_spec2')+"."+request.POST.get('custom_points_system_final_spec3')+"."+request.POST.get('custom_points_system_final_spec4')\
                              +request.POST.get('swiss_final_spec1')+"."+request.POST.get('swiss_final_spec2')+"."+request.POST.get('swiss_final_spec3')+"."+request.POST.get('swiss_final_spec4')+"."+request.POST.get('swiss_final_spec5')
        elif tournament_type == "two_tournament":
            tournament_spec = request.POST.get('single_elimination_group_spec1')+"."+request.POST.get('single_elimination_group_spec2')\
                              +request.POST.get('double_elimination_group_spec1')+"."+request.POST.get('double_elimination_group_spec2')\
                              +request.POST.get('round_robin_group_spec1')+"."+request.POST.get('round_robin_group_spec2')\
                              +request.POST.get('round_robin_group_spec')+"."+request.POST.get('custom_points_system_group_spec1')+"."+request.POST.get('custom_points_system_group_spec2')+"."+request.POST.get('custom_points_system_group_spec3')+"."+request.POST.get('custom_points_system_group_spec4')\
                              +"/"\
                              +request.POST.get('single_elimination_final_spec')+request.POST.get('double_elimination_final_spec')\
                              +request.POST.get('round_robin_final_spec')+"."+request.POST.get('custom_points_system_final_spec1')+"."+request.POST.get('custom_points_system_final_spec2')+"."+request.POST.get('custom_points_system_final_spec3')+"."+request.POST.get('custom_points_system_final_spec4')\
                              +request.POST.get('swiss_final_spec1')+"."+request.POST.get('swiss_final_spec2')+"."+request.POST.get('swiss_final_spec3')+"."+request.POST.get('swiss_final_spec4')+"."+request.POST.get('swiss_final_spec5')

        # 공약 내용 & 후원자 보상 리스트 가져오기
        promise = request.POST.getlist('promise')+"."+request.POST.getlist('promise_spec')
        reward = request.POST.getlist('reward')+"."+request.POST.getlist('reward_spec')

        # 참가자명/팀명(필수), 참가자 연락처, 참가자 이메일, 추가기타양식(input)
        template = request.POST.get('template_name')+"."+request.POST.get('template_phone')+"."+request.POST.get('template_email')+"."+request.POST.get('input_template_etc')

        # save 코드
        tournament_obj = Tournament(username=request.user.username, email=request.user.email, tournament_name=request.POST.get('tournament_name'),
                                    tournament_game=request.POST.get('tournament_game'), tournament_url = request.POST.get('tournament_url'),
                                    streaming_url=request.POST.get('streaming_url'), streaming_url_spec=streaming_url_spec,
                                    tournament_type=tournament_type, tournament_format=tournament_format, tournament_spec=tournament_spec,
                                    registration=request.POST.get('registration'), registration_team=request.POST.get('registration_team'),
                                    participant=request.POST.get('participant'), starttime=request.POST.get('starttime'),
                                    checkin=request.POST.get('checkin'), checkin_time=request.POST.get('checkin_time'), description=request.POST.get('description'),
                                    funding=request.POST.get('funding'), promise=promise, reward=reward, template=template, phone=request.POST.get('phone'))
        tournament_obj.save()

        response = {'status': 'success',
                    'message': "대회 생성 요청이 성공적으로 제출되었습니다. 빠른 시일 내에 운영진과 검토 후 이메일과 연락처로 대회 개최 여부를 말씀드리겠습니다."}
        return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

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

        send_mail(subject, phone+message, email, ['help@openarena.kr'], fail_silently=False)

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
