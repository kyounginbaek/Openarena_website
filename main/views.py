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
        streaming_url_spec = request.POST.get('streaming_url_spec')
        tournament_type = request.POST.get('tournament_type')

        single_tournament_final = request.POST.get('single_tournament_final')
        two_tournament_group = request.POST.get('two_tournament_group')
        two_tournament_group_round_robin = request.POST.get("two_tournament_group_round_robin")
        two_tournament_final = request.POST.get('two_tournament_final')
        two_tournament_final_round_robin = request.POST.get('two_tournament_final_round_robin')

        registration = request.POST.get('registration')
        registration_team = request.POST.get('registration_team')
        participant = request.POST.get('participant')
        starttime = request.POST.get('starttime')
        checkin = request.POST.get('checkin')
        checkin_time = request.POST.get('checkin_time')
        description = request.POST.get('description')
        funding = request.POST.get('funding')
        promise = request.POST.get('promise')
        promise_spec = request.POST.get('promise_spec')
        reward = request.POST.get('reward')
        reward_spec = request.POST.get('reward_spec')
        template = request.POST.get('template')
        phone = request.POST.get('phone')

        if Tournament.objects.filter(tournament_url=tournament_url).exists():
            response = {'status': 'fail', 'message': "이미 존재하는 대회 url입니다.", 'error':'error1'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
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
