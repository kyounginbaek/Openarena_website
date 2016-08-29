import json

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from main.forms import ContactForm
from main.models import Tournament


def home(request):
    return render(request, 'main/home.html', {})

def looking(request):
    return render(request, 'main/looking.html', {})

def making(request):
    if not request.user.is_authenticated():
        messages.success(request, "로그인이 필요한 페이지입니다. 먼저 로그인을 해주세요.")
        return render(request, 'accounts/login.html', {})

    if request.method == 'POST':
        username = request.user.username
        email = request.user.email
        tournament_name = request.POST.get('tournament_name')
        tournament_game = request.POST.get('tournament_game')
        tournament_url = request.POST.get('tournament_url')
        streaming_url = request.POST.get('streaming_url')
        streaming_url_spec = request.POST.get('input_afreecatv')+request.POST.get('input_twitch')

        # 단일 방식 토너먼트(single_tournament) & 혼합 방식 토너먼트(two_tournament)
        tournament_type = request.POST.get('tournament_type')

        # 싱글 엘리미네이션(single_elimination_final) & 더블 엘리미네이션(double_elimination_final) & 라운드 로빈(round_robin_final) & 스위스리그(swiss_final)
        tournament_format = request.POST.get('single_tournament_final')+request.POST.get('two_tournament_group')+request.POST.get('two_tournament_final')

        # 싱글 엘리미네이션 -> 3위 결정전
        # 더블 엘리미네이션 -> 1-2경기, 1경기, 없음
        # 라운드 로빈 -> 등급순위(), 등급순위 -> custom_points 4개 항목
        # 스위스리그 -> 5개 항목 값
        if tournament_type == "single_tournament":
            tournament_spec = request.POST.get('single_elimination_final_spec')+request.POST.get('double_elimination_final_spec')\
                              +request.POST.get('round_robin_final_spec')+request.POST.get('custom_points_system_final_spec1')+request.POST.get('custom_points_system_final_spec2')+request.POST.get('custom_points_system_final_spec3')+request.POST.get('custom_points_system_final_spec4')\
                              +request.POST.get('swiss_final_spec1')+request.POST.get('swiss_final_spec2')+request.POST.get('swiss_final_spec3')+request.POST.get('swiss_final_spec4')+request.POST.get('swiss_final_spec5')
        elif tournament_type == "two_tournament":
            tournament_spec = request.POST.get('single_elimination_group_spec1')+request.POST.get('single_elimination_group_spec2')\
                              +request.POST.get('double_elimination_group_spec1')+request.POST.get('double_elimination_group_spec2')\
                              +request.POST.get('round_robin_group_spec1')+request.POST.get('round_robin_group_spec2')\
                              +request.POST.get('round_robin_group_spec')+request.POST.get('custom_points_system_group_spec1')+request.POST.get('custom_points_system_group_spec2')+request.POST.get('custom_points_system_group_spec3')+request.POST.get('custom_points_system_group_spec4')\
                              +"/"\
                              +request.POST.get('single_elimination_final_spec')+request.POST.get('double_elimination_final_spec')\
                              +request.POST.get('round_robin_final_spec')+request.POST.get('custom_points_system_final_spec1')+request.POST.get('custom_points_system_final_spec2')+request.POST.get('custom_points_system_final_spec3')+request.POST.get('custom_points_system_final_spec4')\
                              +request.POST.get('swiss_final_spec1')+request.POST.get('swiss_final_spec2')+request.POST.get('swiss_final_spec3')+request.POST.get('swiss_final_spec4')+request.POST.get('swiss_final_spec5')

        registration = request.POST.get('registration')
        registration_team = request.POST.get('registration_team')
        participant = request.POST.get('participant')
        starttime = request.POST.get('starttime')
        checkin = request.POST.get('checkin')
        checkin_time = request.POST.get('checkin_time')
        description = request.POST.get('description')
        funding = request.POST.get('funding')

        # 공약 내용 & 후원자 보상 리스트 가져오기
        promise = request.POST.get('promise1')+request.POST.get('promise_spec1')+request.POST.get('promise2')+request.POST.get('promise_spec2')+\
                  request.POST.get('promise3')+request.POST.get('promise_spec3')+request.POST.get('promise4')+request.POST.get('promise_spec4')+\
                  request.POST.get('promise5')+request.POST.get('promise_spec5')+request.POST.get('promise6')+request.POST.get('promise_spec6')+\
                  request.POST.get('promise7')+request.POST.get('promise_spec7')+request.POST.get('promise8')+request.POST.get('promise_spec8')+\
                  request.POST.get('promise9')+request.POST.get('promise_spec9')+request.POST.get('promise10')+request.POST.get('promise_spec10')
        reward = request.POST.get('reward1')+request.POST.get('reward_spec1')+request.POST.get('reward2')+request.POST.get('reward_spec2')+\
                  request.POST.get('reward3')+request.POST.get('reward_spec3')+request.POST.get('reward4')+request.POST.get('reward_spec4')+\
                  request.POST.get('reward5')+request.POST.get('reward_spec5')+request.POST.get('reward6')+request.POST.get('reward_spec6')+\
                  request.POST.get('reward7')+request.POST.get('reward_spec7')+request.POST.get('reward8')+request.POST.get('reward_spec8')+\
                  request.POST.get('reward9')+request.POST.get('reward_spec9')+request.POST.get('reward10')+request.POST.get('reward_spec10')

        # 참가자명/팀명(필수), 참가자 연락처, 참가자 이메일, 추가기타양식(input)
        template = request.POST.get('template_name')+request.POST.get('template_phone')+request.POST.get('template_email')+request.POST.get('input_template_etc')
        phone = request.POST.get('phone')

        if Tournament.objects.filter(tournament_url=tournament_url).exists():
            response = {'status': 'fail', 'message': "이미 존재하는 대회 url입니다.", 'error':'error1'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            # save 코드
            response = {'status': 'success', 'message': "대회 생성 요청이 성공적으로 제출되었습니다. 빠른 시일 내에 운영진 검토 후 이메일과 연락처로 대회 개최 여부를 말씀드리겠습니다."}
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
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'main/contact.html', {})

    return render(request, 'main/contact.html', {})

def help(request):
    return render(request, 'main/help.html', {})
