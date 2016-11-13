import json
import random
import requests
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Making, Funding, Fundingdummy, Participation, Reply, Video
from django.db.models import Sum

def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    whyachi = Making.objects.filter(tournament_name = '2016 BJ아치 LOL 대회').values().get()
    macho = Making.objects.filter(tournament_name = 'MASL 스타2 리그 시즌3').values().get()

    funding = Funding.objects.all()
    total_amount = Funding.objects.all().aggregate(Sum('amount'))

    return render(request, 'main/looking.html', {'whyachi': whyachi, 'macho': macho,
                                                 'funding': funding, 'total_amount': total_amount})

def making(request):
    if not request.user.is_authenticated():
        messages.success(request, "로그인이 필요한 기능입니다.")
        return render(request, 'accounts/login.html', {})

    if request.method == 'POST':
        # 토너먼트 URL 체크
        tournament_url = request.POST.get('tournament_url')
        if Making.objects.filter(tournament_url=tournament_url).exists():
            response = {'status': 'error'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        # 스트리밍 URL 확인
        if request.POST.get('streaming_url')=='afreecatv':
            streaming_url_spec = "http://play.afreecatv.com/"+request.POST.get('input_afreecatv')
        elif request.POST.get('streaming_url')=='twitch':
            streaming_url_spec = "http://www.twitch.tv/"+request.POST.get('input_twitch')
        elif request.POST.get('streaming_url')=='youtube':
            streaming_url_spec = "http://youtube.com/"+request.POST.get('input_youtube')
        elif request.POST.get('streaming_url') == 'facebook':
            streaming_url_spec = "http://facebook.com/"+request.POST.get('input_facebook')

        # 체크인 기능 NULL 방지
        if request.POST.get('checkin') is not None:
            checkin = request.POST.get('checkin')
        else:
            checkin = "no"

        # 참가자명/팀명(필수), 참가자 연락처, 참가자 이메일, 추가 필요양식(input)
        template = "name"
        if request.POST.get('template_email') is not None:
            template += ".email"
        if request.POST.get('template_phone') is not None:
            template += ".phone"
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
        response = {'status': 'success'}
        return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'main/making.html', {})

def video(request):
    return render(request, 'main/video.html', {})

def contents(request):
    video = Video.objects.all()

    return render(request, 'main/contents.html', {'video': video})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def calendar(request):
    return render(request, 'main/calendar.html', {})

def migal(request):
    return render(request, 'main/migal.html', {})

def darkhumor(request):
    making = Making.objects.all()[:1].values().get()
    participation = Participation.objects.all()
    reply = Reply.objects.all()

    top_funding = Funding.objects.all().order_by('-amount')[:3]
    funding = Funding.objects.all()
    total_amount = Funding.objects.all().aggregate(Sum('amount'))

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/darkhumor.html', {'making': making, 'participation': participation, 'reply': reply,
                                                   'top_funding': top_funding, 'funding': funding,
                                                   'total_amount': total_amount, 'has_funded': has_funded})

def whyachi(request):
    if request.method == 'POST':
        if request.POST.get('purpose')=="participation":
            # save 코드
            participation_obj = Participation(tournament_id=2, tournament_name="2016 BJ 아치의 LOL 대회",
                                              username=request.user.username,
                                              name=request.POST.get('participation_name'),
                                              email=request.user.email,
                                              phone=request.POST.get('participation_phone'),
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'))
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose')=="reply":
            # save 코드
            reply_obj = Reply(tournament_id=2, tournament_name="2016 BJ 아치의 LOL 대회",
                              username=request.user.username,
                              comment=request.POST.get('comment'))
            reply_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose')=="funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161111" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": "2016 BJ 아치의 LOL 대회",
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2015-11-30 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(username=request.user.username, email=request.user.email,
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

    making = Making.objects.filter(tournament_name = '2016 BJ아치 LOL 대회').values().get()
    participation = Participation.objects.all()
    reply = Reply.objects.all()

    top_funding = Funding.objects.all().order_by('-amount')[:3]
    funding = Funding.objects.all()
    total_amount = Funding.objects.all().aggregate(Sum('amount'))

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/whyachi.html', {'making': making, 'participation': participation, 'reply': reply,
                                                 'top_funding': top_funding, 'funding': funding,
                                                 'total_amount': total_amount, 'has_funded': has_funded})

def macho(request):
    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=3, tournament_name="MASL 스타2 리그 시즌3",
                                              username=request.user.username,
                                              name=request.POST.get('participation_name'),
                                              email=request.user.email,
                                              phone=request.POST.get('participation_phone'),
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'),
                                              etc3=request.POST.get('participation_etc3'),
                                              etc4=request.POST.get('participation_etc4'))
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "reply":
            # save 코드
            reply_obj = Reply(tournament_id=3, tournament_name="MASL 스타2 리그 시즌3",
                              username=request.user.username,
                              comment=request.POST.get('comment'))
            reply_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161113" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": "마초 스타2 리그(MASL) 시즌3",
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2015-11-30 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(username=request.user.username, email=request.user.email,
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

    making = Making.objects.filter(tournament_name = 'MASL 스타2 리그 시즌3').values().get()
    participation = Participation.objects.all()
    reply = Reply.objects.all()

    top_funding = Funding.objects.all().order_by('-amount')[:3]
    funding = Funding.objects.all()
    total_amount = Funding.objects.all().aggregate(Sum('amount'))

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/macho.html', {'making': making, 'participation': participation, 'reply': reply,
                                               'top_funding': top_funding, 'funding': funding,
                                               'total_amount': total_amount, 'has_funded': has_funded})

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

def privacy(request):
    return render(request, 'main/privacy.html', {})

def agreement(request):
    return render(request, 'main/agreement.html', {})
