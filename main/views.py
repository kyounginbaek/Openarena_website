import json
import random
import requests
import ast

from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from datetime import datetime, timedelta
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

    for making_item in Tournament.objects.filter(confirm='yes').order_by('-created'):
        #starttime = timezone.localtime(datetime.strptime(making_item.starttime, '%Y/%m/%d %H:%M'))
        starttime = datetime.strptime(making_item.tournament_endtime, '%Y/%m/%d %H:%M')
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

    for making_item in Tournament.objects.filter(confirm='yes').order_by('-created'):
        starttime = datetime.strptime(making_item.tournament_endtime, '%Y/%m/%d %H:%M')
        # print('tg -> '+making_item.tournament_game)
        if starttime > datetime.now():
            card_list.append(making_item)
            if making_item.tournament_game == '리그오브레전드￼':
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
    card_list_lol = Making.objects.filter(tournament_game='리그오브레전드￼').order_by('-when')
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

def tournaments_ct(request):

    if request.is_ajax():
        result = {
            'card_list_html':[],
        }

        progress_card_list= list()
        result_card_list= list()

        game = request.GET.get('game')
        order = request.GET.get('order')
        progress = request.GET.get('progress')

        making_item_query_set = None
        if order == 'sponsor':
            making_item_query_set = sorted(Tournament.objects.all(), key=lambda m: -(m.get_fundings_sum()))
            '''
            def sponsor_key(m):
                return m.get_fundings_sum()
            …
            sorted(…, key=sponsor_key)
            '''
        elif order == 'latest':
            making_item_query_set = Tournament.objects.all().order_by('-created')
        elif order == 'deadline':
            making_item_query_set = Tournament.objects.all().order_by('funding_endtime')

        if progress == "progress":
            for making_item in making_item_query_set:
                if making_item.funding_endtime != '-':
                    starttime = datetime.strptime(making_item.funding_endtime, '%Y/%m/%d %H:%M')
                    if starttime > datetime.now():
                        progress_card_list.append(making_item)

        if progress == "end":
            for making_item in making_item_query_set:
                if making_item.funding_endtime != '-':
                    starttime = datetime.strptime(making_item.funding_endtime, '%Y/%m/%d %H:%M')
                    if starttime <= datetime.now():
                        progress_card_list.append(making_item)

        if game == 'whole':
            for making_item in progress_card_list:
                result_card_list.append(making_item)
        else:
            for making_item in progress_card_list:
                if game == making_item.tournament_game:
                    result_card_list.append(making_item)

        #result['card_list'] = result_card_list
        for card in result_card_list:
            result['card_list_html'].append('''
                    <div class="project-card">
                        <div class="card sticky-action">
                            <a href="/t/%s"><div class="card-image waves-effect waves-block waves-light" id="" style="background: url('%s') center center no-repeat; background-size: contain;">
                            </div></a>
                            <div class="progress stat2">
                                <div class="progress-bar progress-bar-warning progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: %s%%;">
                                </div>
                            </div>
                            <div class="card-content-container">
                                <div class="card-content-title">
                                    <div class="card-content-top">
                                        <div class="card-title-container">
                                            <span class="card-title">%s</span>
                                        </div>
                                        <div class="card-dday-container">
                                            <span class="card-dday">%s</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="card-content-bottom">
                                    <div class="card-fundings-container">
                                        <span class="card-fundings">모인 상금 총 %s원</span>
                                    </div>
                                    <div class="detail-button-container">
                                        <span class="card-title activator grey-text text-darken-4 card-title"><i class="fa fa-chevron-circle-up" aria-hidden="true"></i><i class="material-icons right"></i></span>
                                    </div>
                                </div>
                            </div>
                            <div class="card-reveal card-detail">
                                <div class="progress stat2">
                                    <div class="progress-bar progress-bar-warning progress-bar" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: %s%%;">
                                    </div>
                                </div>
                                <div class="card-content-top">
                                    <div class="card-title-container">
                                        <span class="card-title">%s</span>
                                    </div>
                                    <div class="card-dday-container">
                                        <span class="card-dday">%s</span>
                                    </div>
                                </div>
                                <div class="card-content-bottom">
                                    <div class="card-fundings-container">
                                        <span class="card-fundings">모인 상금 총 %s원</span>
                                    </div>
                                    <div class="detail-button-container">
                                        <span class="card-title activator grey-text text-darken-4 card-title"><i class="fa fa-chevron-circle-down" aria-hidden="true"></i><i class="material-icons right"></i></span>
                                    </div>
                                </div>
                                <div class="card-detail-information">
                                    <ul>
                                        <li><div class="card-information-content">대회 일시</div><div class="card-information-data">%s</div></li>
                                        <li><div class="card-information-content">참가 마감</div><div class="card-information-data">%s</div></li>
                                        <!—
                                                    <li><div class="card-information-content">후원 마감</div><div class="card-information-data">%s</div></li>
                                                    —>
                                        <li><div class="card-information-content">후원자수</div><div class="card-information-data">%s명</div></li>
                                        <!—
                                                    <li><div class="card-information-content">보상</div><div class="card-information-data">%s</div></li>
                                                    —>
                                    </ul>
                                    <div class="card-detail-button">
                                        <button type="button" name="" class="sponser-button"><a href="http://openarena.kr/%s">
                                            바로가기</a></button>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
            ''' % (card.tournament_url,
                   card.tournament_image,
                   card.get_fundings_percentage(),
                   card.tournament_name,
                   card.get_day(),
                   card.get_fundings_sum(),
                   card.get_fundings_percentage(),
                   card.tournament_name,
                   card.get_day(),
                   card.get_fundings_sum(),
                   card.tournament_starttime,
                   card.participation_endtime,
                   card.funding_endtime,
                   card.get_funding_num(),
                   card.reward,
                   card.tournament_url
                   ))
        '''
        if order == "sponsor":
#            result_card_list.sorted('when')
            result['card_list'] = sorted(model_to_dict(making_item))

        if order == "latest":
#            result_card_list.order_by('-when')
            result['card_list'] = model_to_dict(making_item)

        if order == "deadline":
#            result_card_list.order_by('when')
            result['card_list'] = model_to_dict(making_item)
        '''
        return JsonResponse(result)
    return HttpResponse("tournament_ct")

def archive(request):
    card_list_end = list()
    for making_item in Tournament.objects.filter(confirm='yes').order_by('-created'):
        starttime = datetime.strptime(making_item.tournament_endtime, '%Y/%m/%d %H:%M')
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
                                        promise_number=request.POST.getlist('promise_number[]'), #array
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

            now = datetime.now().strftime('%Y%m%d%H%M%S')

            # 생성된 챌론지 링크를 업데이트 시키기
            Tournament.objects.filter(id=str(tournament_obj.id)).update(
                challonge_url="openarena_" + str(tournament_obj.id) + "_" + request.POST.get(
                    'tournament_url') + "_" + now)

            # 챌론지 대회 생성
            url = "https://api.challonge.com/v1/tournaments.json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
                "tournament": {
                    "name": request.POST.get('tournament_name'),
                    # "tournament_type": "", # finished
                    "url": "openarena_"+str(tournament_obj.id)+"_"+request.POST.get('tournament_url')+"_"+now,
                    "open_signup": "false",
                    # single elimination only
                    # "hold_third_place_match": "", # finished
                    # swiss only
                    # "pts_for_match_win": "", # finished
                    # "pts_for_match_tie": "", # finished
                    # "pts_for_game_win": "", # finished
                    # "pts_for_game_tie": "", # finished
                    # "pts_for_bye": "", # finished
                    # "swiss_rounds": "" # not yet
                    # "ranked_by": "", # finished
                    # round robin only
                    # "rr_pts_for_match_win": "", # finished
                    # "rr_pts_for_match_tie": "", # finished
                    # "rr_pts_for_game_win": "", # finished
                    # "rr_pts_for_game_tie": "", # finished
                    # sequential_pairings = true & false 가능하도록 변경 필요 # not yet
                    "sequential_pairings": "true",
                    # "signup_cap": "", # finished
                    # double_elimination only
                    # "grand_finals_modifier": "" # finished
                }
            }

            if request.POST.get('tournament_format') == "no":
                data['tournament'].update({'tournament_type': 'single elimination'})
            else:
                if request.POST.get('tournament_format') == 'single_elimination':
                    data['tournament'].update({'tournament_type': 'single elimination'})
                    if request.POST.get('tournament_format_spec') == 'yes_3rd_match':
                        data['tournament'].update({'hold_third_place_match': 'true'})
                elif request.POST.get('tournament_format') == 'double_elimination':
                    data['tournament'].update({'tournament_type': 'double elimination'})
                    if request.POST.get('tournament_format_spec') == 'no_advantage':
                        data['tournament'].update({'grand_finals_modifier': 'single match'})
                    elif request.POST.get('tournament_format_spec') == 'auto_win':
                        data['tournament'].update({'grand_finals_modifier': 'skip'})
                elif request.POST.get('tournament_format') == 'round_robin':
                    data['tournament'].update({'tournament_type': 'round robin'})
                    if request.POST.get('tournament_format_spec') == 'match_wins':
                        data['tournament'].update({'ranked_by': 'match wins'})
                    elif request.POST.get('tournament_format_spec') == 'game_wins':
                        data['tournament'].update({'ranked_by': 'game wins'})
                    elif request.POST.get('tournament_format_spec') == 'points_score':
                        data['tournament'].update({'ranked_by': 'points scored'})
                    elif request.POST.get('tournament_format_spec') == 'points_difference':
                        data['tournament'].update({'ranked_by': 'points difference'})
                    else:
                        array_ast = ast.literal_eval(str(request.POST.getlist('tournament_format_spec[]')))
                        data['tournament'].update({'ranked_by': 'custom'})
                        data['tournament'].update({'rr_pts_for_match_win': array_ast[0]})
                        data['tournament'].update({'rr_pts_for_match_tie': array_ast[1]})
                        data['tournament'].update({'rr_pts_for_game_win': array_ast[2]})
                        data['tournament'].update({'rr_pts_for_game_tie': array_ast[3]})
                elif request.POST.get('tournament_format') == 'swiss':
                    array_ast = ast.literal_eval(str(request.POST.getlist('tournament_format_spec[]')))
                    data['tournament'].update({'tournament_type': 'swiss'})
                    data['tournament'].update({'pts_for_match_win': array_ast[0]})
                    data['tournament'].update({'pts_for_match_tie': array_ast[1]})
                    data['tournament'].update({'pts_for_game_win': array_ast[2]})
                    data['tournament'].update({'pts_for_game_tie': array_ast[3]})
                    data['tournament'].update({'pts_for_bye': array_ast[4]})

            if request.POST.get('participation')=='yes':
                data['tournament'].update({'signup_cap': request.POST.get('participation_number')})

            headers = {'content-type': 'application/json'}
            result = requests.post(url, data=json.dumps(data), headers=headers)

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
            if Participation.objects.filter(tournament_id=request.POST.get('tournament_id'), username=request.user.username).exists():
                response = {'status': 'exist'}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
                template_length = len(ast.literal_eval(tournament.get('participation_template')))

                input = []
                for i in range(1, template_length+1):
                    if request.POST.get('participation_template['+str(i)+']') is not None:
                        input.append(request.POST.get('participation_template['+str(i)+']'))
                    else:
                        file = request.FILES.get('participation_template['+str(i)+']')

                        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
                                            host='s3.ap-northeast-2.amazonaws.com')
                        bucket = conn.get_bucket('openarena')

                        k = Key(bucket)
                        k.key = file.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        k.content_type = 'text/plain'
                        k.set_contents_from_string(file.read(), policy='public-read')
                        url = k.generate_url(expires_in=0, query_auth=False)
                        input.append(url)

                # Challonge 참가자 추가
                url = "https://api.challonge.com/v1/tournaments/" + tournament.get(
                    'challonge_url') + "/participants.json"
                data = {
                    "api_key": settings.CHALLONGE_API_KEY,
                    "participant": {
                        "name": request.user.username
                    }
                }
                headers = {'content-type': 'application/json'}
                result = requests.post(url, data=json.dumps(data), headers=headers)

                participation_obj = Participation(tournament_id=request.POST.get('tournament_id'),
                                                  tournament_name=request.POST.get('tournament_name'),
                                                  username=request.user.username,
                                                  seed=result.json().get('participant').get('seed'),
                                                  challonge_id=result.json().get('participant').get('id'),
                                                  input=input)
                participation_obj.save()

                response = {'status': 'success'}
                return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participationManual":
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
            template_length = len(ast.literal_eval(tournament.get('participation_template')))

            input = []
            for i in range(1, template_length + 1):
                if request.POST.get('participation_template[' + str(i) + ']') is not None:
                    input.append(request.POST.get('participation_template[' + str(i) + ']'))
                else:
                    file = request.FILES.get('participation_template[' + str(i) + ']')

                    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
                                        host='s3.ap-northeast-2.amazonaws.com')
                    bucket = conn.get_bucket('openarena')

                    k = Key(bucket)
                    k.key = file.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    k.content_type = 'text/plain'
                    k.set_contents_from_string(file.read(), policy='public-read')
                    url = k.generate_url(expires_in=0, query_auth=False)
                    input.append(url)

            # Challonge 참가자 추가
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get('challonge_url') + "/participants.json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
                "participant": {
                    "name": request.POST.get('participation_dummy_username')
                }
            }
            headers = {'content-type': 'application/json'}
            result = requests.post(url, data=json.dumps(data), headers=headers)

            participation_obj = Participation(tournament_id=request.POST.get('tournament_id'),
                                              tournament_name=request.POST.get('tournament_name'),
                                              dummy_username=request.POST.get('participation_dummy_username'),
                                              seed=result.json().get('participant').get('seed'),
                                              challonge_id=result.json().get('participant').get('id'),
                                              input=input)
            participation_obj.save()

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participationNo":
            input = request.POST.getlist('participation_input[]')

            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()

            # Challonge 참가자 추가
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get('challonge_url') + "/participants.json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
                "participant": {
                    "name": request.POST.get('participation_dummy_username')
                }
            }
            headers = {'content-type': 'application/json'}
            result = requests.post(url, data=json.dumps(data), headers=headers)

            participation_obj = Participation(tournament_id=request.POST.get('tournament_id'),
                                              tournament_name=request.POST.get('tournament_name'),
                                              dummy_username=request.POST.get('participation_dummy_username'),
                                              seed=result.json().get('participant').get('seed'),
                                              challonge_id=result.json().get('participant').get('id'),
                                              input=input)
            participation_obj.save()

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_edit":
            Participation.objects.filter(id=request.POST.get('participation_id')).update(input=request.POST.getlist('participation_input[]'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_selfedit":
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
            template_length = len(ast.literal_eval(tournament.get('participation_template')))

            input = []
            for i in range(1, template_length + 1):
                if request.POST.get('participation_template[' + str(i) + ']') is not None:
                    input.append(request.POST.get('participation_template[' + str(i) + ']'))
                else:
                    file = request.FILES.get('participation_template[' + str(i) + ']')

                    conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY,
                                        host='s3.ap-northeast-2.amazonaws.com')
                    bucket = conn.get_bucket('openarena')

                    k = Key(bucket)
                    k.key = file.name + " " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    k.content_type = 'text/plain'
                    k.set_contents_from_string(file.read(), policy='public-read')
                    url = k.generate_url(expires_in=0, query_auth=False)
                    input.append(url)

            Participation.objects.filter(tournament_id=request.POST.get('tournament_id'),username=request.user.username).update(
                input=input)
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_delete":
            participation = Participation.objects.filter(id=request.POST.get('participation_id')).values().get()
            participation_all = Participation.objects.filter(tournament_id=request.POST.get('tournament_id'))

            # 대회 참가자 시드 순위 변경
            for p in participation_all.all():
                if p.seed > participation.get('seed'):
                    p.seed = int(p.seed) - 1
                    p.save()

            # 참가자 model 삭제
            Participation.objects.filter(id=request.POST.get('participation_id')).delete()
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()

            # Challonge 참가자 삭제
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get('challonge_url') + "/participants/" + participation.get('challonge_id') + ".json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
            }
            headers = {'content-type': 'application/json'}
            result = requests.delete(url, data=json.dumps(data), headers=headers)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "participation_checkin":
            Participation.objects.filter(tournament_id=request.POST.get('tournament_id'), username=request.user.username).update(
                checkin='확인')
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "challonge_start":
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
            Tournament.objects.filter(id=request.POST.get('tournament_id')).update(challonge_start='yes')

            # Challonge 대회 시작
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get(
                'challonge_url') + "/start.json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
            }
            headers = {'content-type': 'application/json'}
            result = requests.post(url, data=json.dumps(data), headers=headers)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "challonge_restart":
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
            Tournament.objects.filter(id=request.POST.get('tournament_id')).update(challonge_start='-')

            # Challonge 대회 시작
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get(
                'challonge_url') + "/reset.json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
            }
            headers = {'content-type': 'application/json'}
            result = requests.post(url, data=json.dumps(data), headers=headers)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "match_update":
            tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
            match_id = request.POST.get('match_id')

            # Challonge 매치 업데이트
            url = "https://api.challonge.com/v1/tournaments/" + tournament.get(
                'challonge_url') + "/matches/" + match_id + ".json"
            data = {
                "api_key": settings.CHALLONGE_API_KEY,
                "match": {
                    "scores_csv": request.POST.get('match_score1') + "-" + request.POST.get('match_score2'),
                    "winner_id": request.POST.get('winner_id')
                }
            }

            headers = {'content-type': 'application/json'}
            result = requests.put(url, data=json.dumps(data), headers=headers)

            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "funding":
            now = datetime.now().strftime('%Y%m%d%H%M%S')

            if request.POST.get('funding_amount') == "etc":
                funding_amount = request.POST.get('funding_amount_etc')
            else:
                funding_amount = request.POST.get('funding_amount')

            url = "https://toss.im/tosspay/api/v1/payments"
            params = {
                "orderNo": request.POST.get('tournament_id')+"_"+str(request.user.id)+"_"+now,
                "amount": funding_amount,
                "productDesc": request.POST.get('tournament_name'),
                "apiKey": settings.TOSS_API_LIVE_KEY,
                "retUrl": 'http://openarena.kr' + "/funding_success"
            }

            result = requests.post(url, data=params)
            # print(response.text)

            if result.json().get('status') == 200 and result.json().get('code') != -1:
                # save 코드
                funding_obj = Funding(tournament_id=request.POST.get('tournament_id'),
                                      tournament_name=request.POST.get('tournament_name'),
                                      username=request.user.username, email=request.user.email,
                                      comment=request.POST.get('funding_comment'),
                                      phone=request.POST.get('funding_phone'),
                                      orderno=params.get('orderNo'), amount=params.get('amount'))

                # 후원 보상 입력
                # tournament = Tournament.objects.filter(id=request.POST.get('tournament_id')).values().get()
                # reward_number = list(tournament.reward_number)
                # reward_spec = list(tournament.reward_spec)
                # reward = ""
                #
                # index = 0
                # for rn in reward_number:
                #     if funding_amount >= rn:
                #
                #
                #     index += 1

                funding_obj.save()
                response = {'status': result.json().get('checkoutPage')}
                return HttpResponse(json.dumps(response), content_type='application/json')
            else:
                response = {'status': 'fail'}
                return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "notice":
            # save 코드
            Tournament.objects.filter(id=request.POST.get('tournament_id')).update(notice=request.POST.get('notice'))
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        elif request.POST.get('purpose') == "comment":
            # Set a blank path then save it to get an ID
            form = CommentForm()
            temp = form.save(commit=False)
            temp.tournament_id = request.POST.get('tournament_id')
            temp.tournament_name = request.POST.get('tournament_name')
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
        elif request.POST.get('purpose') == "chat":
            response = {'status': 'success'}
            return HttpResponse(json.dumps(response), content_type='application/json')

    tournament = Tournament.objects.filter(tournament_url=url).values().get()
    tournament_id = tournament.get('id')
    tournament_name = tournament.get('tournament_name')
    participation = Participation.objects.filter(tournament_name=tournament_name)
    if request.user.is_authenticated():
        if Participation.objects.filter(tournament_name=tournament_name, username=request.user.username).exists():
            participation_userinfo = Participation.objects.filter(tournament_name=tournament_name, username=request.user.username).values().get()
            participation_userinfo_input_list = ast.literal_eval(participation_userinfo.get('input'))
        else:
            participation_userinfo = ""
            participation_userinfo_input_list = ""
    else:
        participation_userinfo = ""
        participation_userinfo_input_list = ""

    # challonge 대회 매치 정보 가져오기
    url = "https://api.challonge.com/v1/tournaments/" + tournament.get(
        'challonge_url') + "/matches.json"
    data = {
        "api_key": settings.CHALLONGE_API_KEY,
    }
    headers = {'content-type': 'application/json'}
    challonge_match_list = requests.get(url, params=data, headers=headers).json()

    # participation_input = ast.literal_eval(participation.get('input'))
    funding = list(Funding.objects.filter(tournament_id=tournament_id).order_by('-amount'))

    # 토스 후원 목록과 비교하여 후원이 완료되었는지 체크 (confirm = yes, no)
    url = "https://toss.im/tosspay/api/v1/status"
    for f in funding:
        if f.orderno != "admin" and f.orderno != "-" :
            if f.confirm != 'yes':
                params = {
                    "orderNo": f.orderno,
                    "apiKey": settings.TOSS_API_LIVE_KEY
                }
                result = requests.post(url, data=params)
                if result.json().get('code') != 0:
                    funding.remove(f)
                else:
                    f.confirm = 'yes'
                    f.save()

    total_amount = str(sum(f.amount for f in funding))

    # Retrieve all comments and sort them by path
    comment_tree = Comment.objects.filter(tournament_name=tournament_name).order_by('-path')

    # 현재 시간
    now = datetime.now()

    # 대회가 시작했는지 여부 판단
    tournament_start = ""
    if now >= datetime.strptime(tournament.get('tournament_starttime'), '%Y/%m/%d %H:%M'):
        tournament_start = "yes"

    # 대회가 끝났는지 여부 판단
    tournament_finish = ""
    if now >= datetime.strptime(tournament.get('tournament_endtime'), '%Y/%m/%d %H:%M'):
        tournament_finish = "finished"

    # 참가자를 받을 경우, char을 배열로 처리
    participation_template_format = "[]"
    participation_template = "[]"
    participation_finish = ""
    participation_exist = ""
    checkin_start = ""
    if tournament.get('participation') == 'yes':
        participation_template_format = ast.literal_eval(tournament.get('participation_template_format'))
        participation_template = ast.literal_eval(tournament.get('participation_template'))

        # 참가자가 참가 신청을 했는지 여부 판단
        if Participation.objects.filter(tournament_id=tournament_id, username=request.user.username).exists():
            participation_exist = "exist"

        # 참가자 신청 기간이 끝났는지 여부 판단
        participation_endtime = datetime.strptime(tournament.get('participation_endtime'), '%Y/%m/%d %H:%M')
        if now >= participation_endtime:
            participation_finish = "finished"

        # 체크인 시간이 되었는지 여부 판단
        if tournament.get('participation_checkin') != 'no' and tournament.get('participation_checkin') != '-':
            checkin_time = tournament.get('participation_checkin')
            time_diff = timedelta(minutes=0)
            if checkin_time == "15분":
                time_diff = timedelta(minutes=15)
            elif checkin_time == "30분":
                time_diff = timedelta(minutes=30)
            elif checkin_time == "1시간":
                time_diff = timedelta(hours=1)
            elif checkin_time == "2시간":
                time_diff = timedelta(hours=2)
            elif checkin_time == "6시간":
                time_diff = timedelta(hours=6)
            elif checkin_time == "1일":
                time_diff = timedelta(days=1)
            elif checkin_time == "2일":
                time_diff = timedelta(days=2)

            if datetime.strptime(tournament.get('tournament_starttime'), '%Y/%m/%d %H:%M') - now <= time_diff:
                checkin_start = "yes"

    # reward 보상을 할 경우, char을 배열로 처리
    # promise 보상을 할 경우, char을 배열로 처리
    reward_number = "[]"
    reward_spec = "[]"
    promise_number = "[]"
    promise_spec = "[]"
    funding_finish = ""
    if tournament.get('funding') == 'yes':
        if tournament.get('reward') == 'yes':
            reward_number = ast.literal_eval(tournament.get('reward_number'))
            reward_spec = ast.literal_eval(tournament.get('reward_spec'))

        if tournament.get('promise') == 'yes':
            promise_number = ast.literal_eval(tournament.get('promise_number'))
            promise_spec = ast.literal_eval(tournament.get('promise_spec'))

        funding_endtime = datetime.strptime(tournament.get('funding_endtime'), '%Y/%m/%d %H:%M')
        if now >= funding_endtime:
            funding_finish = "finished"

    # streaming을 할 경우, char을 배열로 처리
    if tournament.get('streaming') == 'yes':
        streaming_site = ast.literal_eval(tournament.get('streaming_site'))
        streaming_url = ast.literal_eval(tournament.get('streaming_url'))
    else :
        streaming_site = "[]"
        streaming_url = "[]"

    # video = Video.objects.filter(tournament_name=tournament.get('tournament_name'))

    # 그 사람이 후원했는지를 검색하는 기능
    if Funding.objects.filter(tournament_id=tournament_id, username=request.user.username).exists():
        has_funded = "yes"
    else:
        has_funded = "no"

    # 대회 개최자일 경우, {공지사항, 참가자 명단, 후원자 명단}의 수정이 가능하도록
    if request.user.username == tournament.get('username'):
        is_creator = "yes"
    else:
        is_creator = "no"

    return render(request, 'main/template.html', {'tournament': tournament, 'participation': participation,
                                                  'funding': funding, 'tournament_start': tournament_start,
                                                  'tournament_finish': tournament_finish,
                                                  'comment_tree': comment_tree, 'participation_exist': participation_exist,
                                                  'participation_finish': participation_finish,
                                                  'checkin_start': checkin_start,
                                                  'challonge_match_list': challonge_match_list,
                                                  'participation_userinfo': participation_userinfo,
                                                  'participation_userinfo_input_list': participation_userinfo_input_list,
                                                  'funding_finish': funding_finish, 'has_funded': has_funded,
                                                  'total_amount': total_amount, 'is_creator': is_creator,
                                                  'reward_number': reward_number, 'reward_spec': reward_spec,
                                                  'promise_number': promise_number, 'promise_spec': promise_spec,
                                                  'participation_template_format': participation_template_format,
                                                  'participation_template': participation_template,
                                                  'streaming_site': streaming_site, 'streaming_url': streaming_url})

def members(request):
    return render(request, 'main/members.html', {})

def funding_success(request):


    return render(request, 'main/funding_success.html', {})