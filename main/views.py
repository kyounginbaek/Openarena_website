import json
import random
import requests
import ast
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from datetime import datetime
from main.models import Making, Fundingdummy, Funding, Participation, Video, Privacy, Agreement, Help, Comment, CommentForm, Chat, Gamerule, Tournament
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from django.conf import settings

def home(request):
    card_list_ing = list()
    card_list_end = list()

    for making_item in Making.objects.all().order_by('-when'):
        #starttime = timezone.localtime(datetime.strptime(making_item.starttime, '%Y/%m/%d %H:%M'))
        starttime = datetime.strptime(making_item.funding_endtime, '%Y/%m/%d %H:%M')
        #print('tg -> '+making_item.tournament_game)
        if starttime > datetime.now():
            card_list_ing.append(making_item)
        elif starttime < datetime.now():
            card_list_end.append(making_item)

    participation = Participation.objects.all()

    return render(request, 'main/home.html', {'card_list_ing': card_list_ing, 'participation': participation, 'card_list_end': card_list_end, })

def tournaments(request):
    # card_list = Making.objects.filter(starttime__gt=datetime.now()).order_by('-when')
    card_list = list()
    card_list_lol = list()
    card_list_overwatch = list()
    card_list_star2 = list()
    card_list_heartstone = list()
    card_list_shadowverse = list()

    for making_item in Making.objects.all().order_by('-when'):
        starttime = datetime.strptime(making_item.funding_endtime, '%Y/%m/%d %H:%M')
        # print('tg -> '+making_item.tournament_game)
        if starttime > datetime.now():
            card_list.append(making_item)
            if making_item.tournament_game == '리그오브레전드(LOL)':
                card_list_lol.append(making_item)
            elif making_item.tournament_game == '오버워치':
                card_list_overwatch.append(making_item)
            elif making_item.tournament_game == '스타크래프트2':
                card_list_star2.append(making_item)
            elif making_item.tournament_game == '하스스톤':
                card_list_heartstone.append(making_item)
            elif making_item.tournament_game == '섀도우버스':
                card_list_shadowverse.append(making_item)

    '''
    card_list_lol = Making.objects.filter(tournament_game='리그오브레전드(LOL)').order_by('-when')
    card_list_overwatch = Making.objects.filter(tournament_game='오버워치', starttime__gt=datetime.now()).order_by('-when')
    card_list_star2 = Making.objects.filter(tournament_game='스타크래프트2', starttime__gt=datetime.now()).order_by('-when')
    card_list_heartstone = Making.objects.filter(tournament_game='하스스톤', starttime__gt=datetime.now()).order_by('-when')
    card_list_shadowverse = Making.objects.filter(tournament_game='섀도우버스', starttime__gt=datetime.now()).order_by('-when')
    '''

    # print(card_list)

    context = {
        'card_list': card_list,
        'card_list_lol': card_list_lol,
        'card_list_overwatch': card_list_overwatch,
        'card_list_star2': card_list_star2,
        'card_list_heartstone': card_list_heartstone,
        'card_list_shadowverse': card_list_shadowverse,
    }

    return render(request, 'main/tournaments.html', context)

def archive(request):
    card_list_end = list()
    for making_item in Making.objects.all().order_by('-when'):
        starttime = datetime.strptime(making_item.funding_endtime, '%Y/%m/%d %H:%M')
        #starttime = datetime.strptime(making_item.starttime, '%Y/%m/%d %H:%M')
        if starttime <= datetime.now():
            card_list_end.append(making_item)

    return render(request, 'main/archive.html', {'card_list_end': card_list_end,})

def clubs(request):
    return render(request, 'main/clubs.html', {})

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
        tournament_obj = Making(username=request.user.username, email=request.user.email, tournament_name=request.POST.get('tournament_name'),
                                tournament_game=request.POST.get('tournament_game'), tournament_url = request.POST.get('tournament_url'),
                                streaming_url=request.POST.get('streaming_url'), streaming_url_spec=streaming_url_spec,
                                registration=request.POST.get('registration'), registration_team=request.POST.get('registration_team'),
                                participant=request.POST.get('participant'), starttime=request.POST.get('starttime'), funding_goal=request.POST.get('funding_goal'),
                                checkin=checkin, checkin_time=request.POST.get('checkin_time'), description=request.POST.get('description'),
                                promise=request.POST.getlist('promise[]'), promise_spec= request.POST.getlist('promise_spec[]'), reward=request.POST.getlist('reward[]'), reward_spec=request.POST.getlist('reward_spec[]'),
                                template=template, phone=request.POST.get('phone'))
        tournament_obj.save()
        response = {'status': 'success'}
        return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'main/making.html', {})

def hallfame(request):
    return render(request, 'main/hallfame.html', {})

def calendar(request):
    return render(request, 'main/calendar.html', {})

@csrf_exempt
def migal(request):
    tournament_name = "BJ최미갈의 레전드 매치"
    if request.method == 'POST':
        if request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161111" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2016-11-30 19:00:00",
            }
            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Funding(tournament_id=2, tournament_name=tournament_name,
                                      username=request.user.username, email=request.user.email,
                                      orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:3]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/migal.html', {'tournament': tournament, 'participation': participation,
                                               'top_funding': top_funding, 'funding': funding,
                                               'total_amount': total_amount, 'has_funded': has_funded,
                                               'video': video})

@csrf_exempt
def whyachi(request):
    tournament_name = "2016 BJ아치 LOL 대회"
    if request.method == 'POST':
        if request.POST.get('purpose')=="participation":
            # save 코드
            participation_obj = Participation(tournament_id=2, tournament_name=tournament_name,
                                              username=request.user.username,
                                              name=request.POST.get('participation_name'),
                                              email=request.user.email,
                                              phone=request.POST.get('participation_phone'),
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'))
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose')=="funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161111" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2016-11-30 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Funding(tournament_id=2, tournament_name=tournament_name,
                                      username=request.user.username, email=request.user.email,
                                      orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:3]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/whyachi.html', {'tournament': tournament, 'participation': participation,
                                                 'top_funding': top_funding, 'funding': funding,
                                                 'total_amount': total_amount, 'has_funded': has_funded,
                                                 'video': video})

@csrf_exempt
def macho(request):
    tournament_name = "MC마초 스타2리그 시즌3"
    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=3, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161113" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2016-11-30 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Funding(tournament_id=3, tournament_name=tournament_name,
                                      username=request.user.username, email=request.user.email,
                                      orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:4]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/macho.html', {'tournament': tournament, 'participation': participation,
                                               'top_funding': top_funding, 'funding': funding,
                                               'total_amount': total_amount, 'has_funded': has_funded,
                                               'video': video})

@csrf_exempt
def macho2(request):
    tournament_name = "MC마초 스타2 연승전"

    chat = Chat.objects.all()
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.all().order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=4, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20161228" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-01-31 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Funding(tournament_id=3, tournament_name=tournament_name,
                                      username=request.user.username, email=request.user.email,
                                      comment=request.POST.get('funding_comment'),
                                      orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = get_object_or_404(Making, tournament_name=tournament_name)
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:4]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/macho2.html', {'tournament': tournament, 'participation': participation,
                                                'top_funding': top_funding, 'funding': funding,
                                                'total_amount': total_amount, 'has_funded': has_funded,
                                                'chat': chat, 'comment_tree': comment_tree, 'video': video})

@csrf_exempt
def scc2(request):
    tournament_name = "제2회 Slayer Conqueror Cup"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=5, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170129" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-01-31 19:00:00",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=5, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = get_object_or_404(Making, tournament_name=tournament_name)
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:4]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    return render(request, 'main/scc2.html', {'tournament': tournament, 'participation': participation,
                                              'top_funding': top_funding, 'funding': funding,
                                              'total_amount': total_amount, 'has_funded': has_funded,
                                              'chat': chat, 'comment_tree': comment_tree, 'video': video})

@csrf_exempt
def vsc(request):
    tournament_id = 6
    tournament_name = "2017 Versestop Shadowverse Cup"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170217" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-02-28 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/vsc.html', {'tournament': tournament, 'participation': participation,
                                             'top_funding': top_funding, 'funding': funding,
                                             'total_amount': total_amount, 'has_funded': has_funded,
                                             'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def ringoncup(request):
    tournament_id = 7
    tournament_name = "제2회 섀도우버스 링곤컵"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
                                              username=request.user.username,
                                              email=request.user.email,
                                              phone=request.POST.get('participation_phone'),
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'),
                                              etc3=request.POST.get('participation_etc3'))
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170219" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/ringoncup.html', {'tournament': tournament, 'participation': participation,
                                                   'top_funding': top_funding, 'funding': funding,
                                                   'total_amount': total_amount, 'has_funded': has_funded,
                                                   'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def scc3(request):
    tournament_id = 8
    tournament_name = "제3회 Slayer Conqueror Cup"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170220" + str(random.randrange(1, 99999999)),
                "amount": request.POST.get('funding_amount'),
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/scc3.html', {'tournament': tournament, 'participation': participation,
                                              'top_funding': top_funding, 'funding': funding,
                                              'total_amount': total_amount, 'has_funded': has_funded,
                                              'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def chainkiller_s1(request):
    tournament_id = 9
    tournament_name = "Chainkiller S1 연승전"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            if(request.POST.get('participation_etc1')=="etc"):
                etc1 = request.POST.get('participation_etc1_etc')
            else:
                etc1 = request.POST.get('participation_etc1')

            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
                                              username=request.user.username,
                                              email=request.user.email,
                                              etc1=etc1,
                                              etc2=request.POST.get('participation_etc2'),
                                              etc3=request.POST.get('participation_etc3'),
                                              etc4=request.POST.get('participation_etc4'),
                                              etc5=request.POST.get('participation_etc5'),
                                              etc6=request.POST.get('participation_etc6'))
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            if (request.POST.get('funding_amount')=="etc"):
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170227" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/chainkiller_s1.html', {'tournament': tournament, 'participation': participation,
                                                        'top_funding': top_funding, 'funding': funding,
                                                        'total_amount': total_amount, 'has_funded': has_funded,
                                                        'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def vsc2(request):
    tournament_id = 10
    tournament_name = "제2회 Versestop Shadowverse Cup"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170311" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/vsc2.html', {'tournament': tournament, 'participation': participation,
                                              'top_funding': top_funding, 'funding': funding,
                                              'total_amount': total_amount, 'has_funded': has_funded,
                                              'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def moon(request):
    tournament_id = 11
    tournament_name = "Moon 클랜 스타 리그"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170312" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/moon.html', {'tournament': tournament, 'participation': participation,
                                              'top_funding': top_funding, 'funding': funding,
                                              'total_amount': total_amount, 'has_funded': has_funded,
                                              'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def scc4(request):
    tournament_id = 12
    tournament_name = "제4회 Slayer Conqueror Cup"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
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
        elif request.POST.get('purpose') == "funding":
            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170321" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           comment2=request.POST.get('funding_comment2'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/scc4.html', {'tournament': tournament, 'participation': participation,
                                              'top_funding': top_funding, 'funding': funding,
                                              'total_amount': total_amount, 'has_funded': has_funded,
                                              'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def hstalk(request):
    tournament_id = 13
    tournament_name = "하스톡방 운고로 최고의 덱메이킹 가려라!"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
                                              username=request.user.username,
                                              email=request.user.email,
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'),
                                              etc3="")
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "image_upload":
            form = UploadFileForm()
            temp = form.save(commit=False)
            file = request.FILES['participation_etc3']

            conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
                                host='s3.ap-northeast-2.amazonaws.com')
            bucket = conn.get_bucket('openarena')

            k = Key(bucket)
            k.key = file.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            k.content_type = 'text/plain'
            k.set_contents_from_string(file.read(), policy='public-read')
            url = k.generate_url(expires_in=0, query_auth=False)
            Participation.objects.filter(tournament_name=tournament_name, username=request.user.username, etc1=request.POST.get('participation_etc1')).update(etc3=url)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170321" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-03-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           comment2=request.POST.get('funding_comment2'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/hstalk.html', {'tournament': tournament, 'participation': participation,
                                                'top_funding': top_funding, 'funding': funding,
                                                'total_amount': total_amount, 'has_funded': has_funded,
                                                'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

@csrf_exempt
def onfps(request):
    tournament_id = 14
    tournament_name = "온님 TV FPS 토너먼트 CS:GO Season 5"

    chat = Chat.objects.filter(tournament_name=tournament_name)
    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            # save 코드
            participation_obj = Participation(tournament_id=tournament_id, tournament_name=tournament_name,
                                              username=request.user.username,
                                              email=request.user.email,
                                              etc1=request.POST.get('participation_etc1'),
                                              etc2=request.POST.get('participation_etc2'),
                                              etc3="")
            participation_obj.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "image_upload":
            form = UploadFileForm()
            temp = form.save(commit=False)
            file = request.FILES['participation_etc3']

            conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
                                host='s3.ap-northeast-2.amazonaws.com')
            bucket = conn.get_bucket('openarena')

            k = Key(bucket)
            k.key = file.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            k.content_type = 'text/plain'
            k.set_contents_from_string(file.read(), policy='public-read')
            url = k.generate_url(expires_in=0, query_auth=False)
            Participation.objects.filter(tournament_name=tournament_name, username=request.user.username, etc1=request.POST.get('participation_etc1')).update(etc3=url)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": "20170325" + str(random.randrange(1, 99999999)),
                "amount": funding_amount,
                "productDesc": tournament_name,
                "apiKey": "sk_live_ePk39VmNdnePk39VmNdn",
                "expiredTime": "2017-05-31 23:59:59",
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Fundingdummy(tournament_id=tournament_id, tournament_name=tournament_name,
                                           username=request.user.username, email=request.user.email,
                                           comment=request.POST.get('funding_comment'),
                                           orderno=params.get('orderNo'), amount=params.get('amount'))
                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "description":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(description=request.POST.get('description'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "notice":
            # save 코드
            Making.objects.filter(tournament_name=tournament_name).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "chat":
            msg = request.POST.get('msgbox', None)
            c = Chat(user=request.user, message=msg)
            if msg != '':
                c.save()

            response = {'msg': msg, 'user': c.user.username}
            return HttpResponse(json.dumps(response), content_type='application/json')

        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_name = tournament_name
            temp.username = request.user.username
            temp.content = request.POST.get('content')
            temp.save()

            id = int(temp.id)
            parent = request.POST.get('parent')
            if parent == '':
                # converting ID to int because save() gives a long int ID
                temp.path = [id]
            else:
                # Get the parent node
                parent_obj = Comment.objects.get(id=parent)
                temp.depth = int(parent_obj.depth) + 1
                s = str(parent_obj.path)
                temp.path = eval(s)
                # Store parents path then apply comment ID
                temp.path.append(id)

            temp.save()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Making.objects.filter(tournament_name=tournament_name).values().get()
    participation = Participation.objects.filter(tournament_name=tournament_name)

    top_funding = Funding.objects.filter(tournament_name=tournament_name).order_by('-amount')[:5]
    funding = Funding.objects.filter(tournament_name=tournament_name)
    total_amount = Funding.objects.filter(tournament_name=tournament_name).aggregate(Sum('amount'))

    video = Video.objects.filter(tournament_name=tournament_name)

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우 공지사항 수정 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/onfps.html', {'tournament': tournament, 'participation': participation,
                                               'top_funding': top_funding, 'funding': funding,
                                               'total_amount': total_amount, 'has_funded': has_funded,
                                               'chat': chat, 'comment_tree': comment_tree, 'video': video, 'is_creator': is_creator})

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

@csrf_exempt
def privacy(request):
    if request.method == 'POST':
        if request.POST.get('purpose') == "content_change":
            # save 코드
            Privacy.objects.update(content=request.POST.get('content'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    privacy = Privacy.objects.values().get()
    return render(request, 'main/privacy.html', {'privacy': privacy})

@csrf_exempt
def agreement(request):
    if request.method == 'POST':
        if request.POST.get('purpose') == "content_change":
            # save 코드
            Agreement.objects.update(content=request.POST.get('content'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
    agreement = Agreement.objects.values().get()
    return render(request, 'main/agreement.html', {'agreement': agreement})

def help(request):
    help_type1 = Help.objects.filter(type=1)
    help_type2 = Help.objects.filter(type=2)
    help_type3 = Help.objects.filter(type=3)
    return render(request, 'main/help.html', {'help_type1': help_type1,
                                              'help_type2': help_type2,
                                              'help_type3': help_type3})

def chat(request):
    c = Chat.objects.all()
    return render(request, 'main/functions/messages.html', {'chat': c})

@csrf_exempt
def create(request):
    gamerule = Gamerule.objects.all()
    if request.method == 'POST':
        if request.POST.get('purpose') == "tournament_name":
            # 중복되는 tournament_name 있는지 확인
            if Tournament.objects.filter(tournament_name=request.POST.get('tournament_name')).exists():
                response = {'status': 'error', 'purpose': 'tournament_name'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'success', 'purpose': 'tournament_name'}
                return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "tournament_url":
            # 중복되는 tournament_name 있는지 확인
            if Tournament.objects.filter(tournament_url=request.POST.get('tournament_url')).exists():
                response = {'status': 'error', 'purpose': 'tournament_url'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'success', 'purpose': 'tournament_url'}
                return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "submit":
            # 대회 생성 및 저장
            # save 코드
            if request.POST.get('tournament_format') == "round_robin":
                if request.POST.get('tournament_format_spec') == "match_wins":
                    tournament_format_spec = request.POST.get('tournament_format_spec')
                elif request.POST.get('tournament_format_spec') == "game_wins":
                    tournament_format_spec = request.POST.get('tournament_format_spec')
                elif request.POST.get('tournament_format_spec') == "points_scored":
                    tournament_format_spec = request.POST.get('tournament_format_spec')
                elif request.POST.get('tournament_format_spec') == "points_difference":
                    tournament_format_spec = request.POST.get('tournament_format_spec')
                else :
                    tournament_format_spec = request.POST.getlist('tournament_format_spec[]')
            elif request.POST.get('tournament_format') == "swiss":
                tournament_format_spec = request.POST.getlist('tournament_format_spec[]')
            else :
                tournament_format_spec = request.POST.get('tournament_format_spec')

            tournament_obj = Tournament(username=request.user.username,
                                        email=request.user.email,
                                        # tab1
                                        tournament_name=request.POST.get('tournament_name'),
                                        tournament_game=request.POST.get('tournament_game'),
                                        tournament_image=request.POST.get('tournament_image'),
                                        tournament_summary=request.POST.get('tournament_summary'),
                                        tournament_url=request.POST.get('tournament_url'),
                                        # tab2
                                        tournament_starttime=request.POST.get('tournament_starttime'),
                                        tournament_endtime=request.POST.get('tournament_endtime'),
                                        tournament_format=request.POST.get('tournament_format'),
                                        tournament_format_spec=tournament_format_spec, #string or array
                                        tournament_rule=request.POST.get('tournament_rule'),
                                        participation=request.POST.get('participation'),
                                        participation_custom_url=request.POST.get('participation_custom_url'),
                                        # participation=yes
                                        participation_type=request.POST.get('participation_type'),
                                        participation_template_custom=request.POST.get('participation_template_custom'),
                                        participation_template_format=request.POST.getlist('participation_template_format[]'), #array
                                        participation_template=request.POST.getlist('participation_template[]'), #array
                                        participation_number=request.POST.get('participation_number'),
                                        participation_time=request.POST.get('participation_time'),
                                        participation_starttime=request.POST.get('participation_starttime'),
                                        participation_endtime=request.POST.get('participation_endtime'),
                                        participation_checkin=request.POST.get('participation_checkin'),
                                        # tab3
                                        funding_notice=request.POST.get('funding_notice'),
                                        account_notice=request.POST.get('account_notice'),
                                        participation_fee=request.POST.get('participation_fee'),
                                        funding=request.POST.get('funding'),
                                        # if funding=yes
                                        funding_goal=request.POST.get('funding_goal'),
                                        funding_time=request.POST.get('funding_time'),
                                        funding_starttime=request.POST.get('funding_starttime'),
                                        funding_endtime=request.POST.get('funding_endtime'),
                                        reward=request.POST.get('reward'),
                                        reward_number=request.POST.getlist('reward_number[]'), #array
                                        reward_spec=request.POST.getlist('reward_spec[]'), #array
                                        promise=request.POST.get('promise'),
                                        promise_number=request.POST.getlist('prosmie_number[]'), #array
                                        promise_spec=request.POST.getlist('promise_spec[]'), #array
                                        # tab4
                                        profile_name=request.POST.get('profile_name'),
                                        profile_introduction=request.POST.get('profile_introduction'),
                                        profile_image=request.POST.get('profile_image'),
                                        streaming=request.POST.get('streaming'),
                                        streaming_site=request.POST.getlist('streaming_site[]'), #array
                                        streaming_url=request.POST.getlist('streaming_url[]'), #array
                                        profile_email=request.POST.get('profile_email'),
                                        profile_phone=request.POST.get('profile_phone'),
                                        profile_account=request.POST.get('profile_account'),
                                        creator_enrollment=request.POST.get('creator_enrollment'))
            tournament_obj.save()

            # 챌론지 대회 생성?

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "image_upload":
            # 이미지 업로드
            form = UploadFileForm()
            temp = form.save(commit=False)
            conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host='s3.ap-northeast-2.amazonaws.com')
            bucket = conn.get_bucket('openarena')

            if request.POST.get('tournament_image_question') != "no":
                file1 = request.FILES['tournament_image']
                k1 = Key(bucket)
                k1.key = file1.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                k1.content_type = 'text/plain'
                k1.set_contents_from_string(file1.read(), policy='public-read')
                url1 = k1.generate_url(expires_in=0, query_auth=False)
                Tournament.objects.filter(tournament_name=request.POST.get('tournament_name')).update(tournament_image=url1)

            if request.POST.get('profile_image_question') != "no":
                file2 = request.FILES['profile_image']
                k2 = Key(bucket)
                k2.key = file2.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                k2.content_type = 'text/plain'
                k2.set_contents_from_string(file2.read(), policy='public-read')
                url2 = k2.generate_url(expires_in=0, query_auth=False)
                Tournament.objects.filter(tournament_name=request.POST.get('tournament_name')).update(profile_image=url2)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    return render(request, 'main/create.html', {'gamerule': gamerule})

@csrf_exempt
def t(request, url):
    if request.method == 'POST':
        if request.POST.get('purpose') == "participation":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "image_upload":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "notice":
            # save 코드
            Tournament.objects.filter(id=request.POST.get('tournament_id')).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "comment":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "chat":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_edit":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_delete":
            Participation.objects.filter(id=request.POST.get('id')).delete()
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Tournament.objects.filter(tournament_url=url).values().get()
    participation = Participation.objects.filter(tournament_name=tournament.get('tournament_name'))
    # participation_input = ast.literal_eval(participation.get('input'))
    funding = Funding.objects.filter(tournament_name=tournament.get('tournament_name')).order_by('-amount')
    total_amount = Funding.objects.filter(tournament_name=tournament.get('tournament_name')).aggregate(Sum('amount'))

    # reward 보상을 할 경우, char을 배열로 처리
    if tournament.get('reward') == 'yes':
        reward_number = ast.literal_eval(tournament.get('reward_number'))
        reward_spec = ast.literal_eval(tournament.get('reward_spec'))
    else:
        reward_number = "[]"
        reward_spec = "[]"

    # reward 보상을 할 경우, char을 배열로 처리
    if tournament.get('promise') == 'yes':
        promise_number = ast.literal_eval(tournament.get('promise_number'))
        promise_spec = ast.literal_eval(tournament.get('promise_spec'))
    else:
        promise_number = "[]"
        promise_spec = "[]"

    # 참가자를 받을 경우, char을 배열로 처리
    if tournament.get('participation') == 'yes':
        participation_template_format = ast.literal_eval(tournament.get('participation_template_format'))
        participation_template = ast.literal_eval(tournament.get('participation_template'))
    else:
        participation_template_format = "[]"
        participation_template = "[]"

    # streaming을 할 경우, char을 배열로 처리
    if tournament.get('streaming') == 'yes':
        streaming_site = ast.literal_eval(tournament.get('streaming_site'))
        streaming_url = ast.literal_eval(tournament.get('streaming_url'))
    else :
        streaming_site = "[]"
        streaming_url = "[]"

    # video = Video.objects.filter(tournament_name=tournament.get('tournament_name'))

    # 대회 개최자일 경우, {공지사항, 참가자 명단, 후원자 명단}의 수정이 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/template.html', {'tournament': tournament, 'participation': participation,
                                                  'funding': funding, #'participation_input': participation_input,
                                                  'total_amount': total_amount, 'is_creator': is_creator,
                                                  'reward_number': reward_number, 'reward_spec': reward_spec,
                                                  'promise_number': promise_number, 'promise_spec': promise_spec,
                                                  'participation_template_format': participation_template_format,
                                                  'participation_template': participation_template,
                                                  'streaming_site': streaming_site, 'streaming_url': streaming_url})

@csrf_exempt
def test(request):
    if request.method == 'POST':
        form = UploadFileForm()
        temp = form.save(commit=False)
        file = request.FILES['tournament_image']

        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host='s3.ap-northeast-2.amazonaws.com')
        bucket = conn.get_bucket('openarena')

        k = Key(bucket)
        k.key = file.name
        k.content_type = 'text/plain'
        k.set_contents_from_string(file.read(), policy='public-read')
        url = k.generate_url(expires_in=0, query_auth=False)

        response = {'status': 'success',
                    'message': url}
        return HttpResponse(json.dumps(response), content_type='application/json')
    return render(request, 'main/test.html', {})

def members(request):
    return render(request, 'main/members.html', {})