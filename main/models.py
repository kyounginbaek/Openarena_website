from django.utils import timezone
from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django_summernote import fields as summer_fields
import ast

class Fundingdummy(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=200, default='')
    tournament_name = models.CharField(max_length=400, default='')
    username = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')
    amount = models.IntegerField(default=0)
    reward = models.CharField(max_length=1000, default='-')
    comment = models.TextField(default='-')
    comment2 = models.TextField(default='-')
    orderno = models.CharField(max_length=400, default='-')
    when = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))
    thanks = models.CharField(max_length=200, default='-')

class Funding(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=200, default='')
    tournament_name = models.CharField(max_length=400, default='')
    username = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')
    amount = models.IntegerField(default=0)
    reward = models.CharField(max_length=1000, default='-')
    phone = models.CharField(max_length=200, default='')
    comment = models.TextField(default='-')
    comment2 = models.TextField(default='-')
    orderno = models.CharField(max_length=400, default='-')
    confirm = models.CharField(max_length=200, default='')
    when = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))
    thanks = models.CharField(max_length=200, default='-')

class Making(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')
    when = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))
    tournament_name = models.CharField(max_length=400, default='')
    tournament_game = models.CharField(max_length=200, default='')
    tournament_url = models.CharField(max_length=200, default='')
    streaming_url = models.CharField(max_length=200, default='')
    streaming_url_spec = models.CharField(max_length=400, default='')
    registration = models.CharField(max_length=200, default='')
    registration_team = models.CharField(max_length=200, default='')
    participant = models.CharField(max_length=200, default='')
    starttime = models.CharField(max_length=200, default='')
    checkin = models.CharField(max_length=200, default='')
    checkin_time = models.CharField(max_length=200, default='')
    description = summer_fields.SummernoteTextField()
    funding_goal = models.CharField(max_length=200, default='')
    promise = models.CharField(max_length=200, default='')
    promise_spec = models.CharField(max_length=200, default='')
    reward = models.CharField(max_length=200, default='')
    reward_spec = models.CharField(max_length=200, default='')
    template = models.CharField(max_length=400, default='')
    phone = models.CharField(max_length=200, default='')
    confirm = models.CharField(max_length=200, default='')

    notice = summer_fields.SummernoteTextField()
    funding_endtime = models.CharField(max_length=200, default='')
    participation_endtime = models.CharField(max_length=200, default='')
    summary = models.TextField(default='')
    main_image = models.CharField(max_length=1000, default='')
    cover_image = models.CharField(max_length=1000, default='')
    poster_image = models.CharField(max_length=1000, default='')
    match_image = models.CharField(max_length=1000, default='')

    def get_fundings_sum(self):
        try:
            funding_sum = 0
            fundings = list()
            for funding in Funding.objects.filter(tournament_name=self.tournament_name):
                fundings.append(funding)
                # print(funding.amount)
            for funding_amount in fundings:
                funding_sum = funding_sum + funding_amount.amount
            return funding_sum
        except ValueError:
            return '-'

    def get_fundings_percentage(self):
        try:
            funding_sum = 0
            fundings = list()
            for funding in Funding.objects.filter(tournament_name=self.tournament_name):
                fundings.append(funding)
            for funding_amount in fundings:
                funding_sum = funding_sum + funding_amount.amount
            funding_rate = funding_sum / int(self.funding_goal) * 100
            return funding_rate
        except ValueError:
            return '-'

            # d_day 연산
    def get_day(self):
        now = datetime.now()
        # print(self.starttime)
        try:
            end_time = datetime.strptime(self.starttime, '%Y/%m/%d %H:%M')
            d_day = str(-(end_time-now).days)
            if not d_day.startswith('-'):
                d_day = '+' + d_day
            return 'D'+d_day
        except ValueError:
            return 'D-X'

    def get_participation(self):
        participation_qs = list()
        for participation in Participation.objects.filter(tournament_name=self.tournament_name):
            participation_qs.append(participation)

        participation_num = len(participation_qs)
        return participation_num

    def get_funding_num(self):
        funding_qs = list()
        for funding in Funding.objects.filter(tournament_name=self.tournament_name):
            funding_qs.append(funding)

        funding_num = len(funding_qs)
        if funding_num == '':
            return 0
        return funding_num

class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')
    created = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))
    # tab1
    tournament_name = models.CharField(max_length=400, default='')
    tournament_game = models.CharField(max_length=400, default='')
    tournament_image = models.CharField(max_length=2000, default='')  # URL or no
    tournament_summary = summer_fields.SummernoteTextField()
    tournament_url = models.CharField(max_length=400, default='')
    # tab2
    tournament_starttime = models.CharField(max_length=200, default='')
    tournament_endtime = models.CharField(max_length=200, default='')
    tournament_format = models.CharField(max_length=200, default='')
    tournament_format_spec = models.CharField(max_length=200, default='-')
    tournament_rule = summer_fields.SummernoteTextField()
    participation = models.CharField(max_length=200, default='')  # yes or no
    participation_custom_url = models.CharField(max_length=2000, default='-')
    # if tournament_registration = yes
    participation_type = models.CharField(max_length=200, default='-')  # individual or team
    participation_template_custom = models.CharField(max_length=200, default='-')  # yes or no
    participation_template_format = models.CharField(max_length=2000, default='[]')  # text or file, array
    participation_template = models.CharField(max_length=2000, default='[]')  # array
    participation_number = models.CharField(max_length=200, default='-')
    participation_time = models.CharField(max_length=200, default='-')  # default or custom
    # if participation_time = custom
    participation_starttime = models.CharField(max_length=200, default='-')
    participation_endtime = models.CharField(max_length=200, default='-')
    participation_checkin = models.CharField(max_length=200, default='-')  # checkin_time or no
    # tab3
    funding_notice = models.CharField(max_length=200, default='-')  # only yes
    account_notice = models.CharField(max_length=200, default='-')  # only yes
    participation_fee = models.CharField(max_length=200, default='-')  # fee_number or no
    funding = models.CharField(max_length=200, default='-')  # yes or no
    # if funding = yes
    funding_goal = models.CharField(max_length=200, default='-')
    funding_time = models.CharField(max_length=200, default='-')  # default or custom
    # if funding_time = custom
    funding_starttime = models.CharField(max_length=200, default='-')
    funding_endtime = models.CharField(max_length=200, default='-')
    reward = models.CharField(max_length=200, default='-')  # yes or no
    reward_number = models.CharField(max_length=4000, default='[]')
    reward_spec = models.CharField(max_length=4000, default='[]')
    promise = models.CharField(max_length=200, default='-')  # yes or no
    promise_number = models.CharField(max_length=4000, default='[]')
    promise_spec = models.CharField(max_length=4000, default='[]')
    # tab4
    profile_name = models.CharField(max_length=400, default='')
    profile_introduction = summer_fields.SummernoteTextField()
    profile_image = models.CharField(max_length=2000, default='')  # URL or no
    streaming = models.CharField(max_length=200, default='')  # yes or no
    streaming_site = models.CharField(max_length=4000, default='')
    streaming_url = models.CharField(max_length=4000, default='')
    profile_email = models.CharField(max_length=400, default='')
    profile_phone = models.CharField(max_length=200, default='-')
    profile_account = models.CharField(max_length=400, default='-')
    donation = models.CharField(max_length=200, default='')  # yes or no
    donation_site = models.CharField(max_length=4000, default='')
    donation_url = models.CharField(max_length=4000, default='')
    creator_enrollment = models.CharField(max_length=200, default='')
    # after submit
    confirm = models.CharField(max_length=200, default='-')  # yes or no(reviewing)
    # template
    cover_image = models.CharField(max_length=2000, default='-')
    logo_image = models.CharField(max_length=2000, default='-')
    challonge_url = models.CharField(max_length=2000, default='-')
    challonge_start = models.CharField(max_length=200, default='-')
    notice = summer_fields.SummernoteTextField(default='공지사항 및 변경사항을 입력해주세요.')
    video_url = models.CharField(max_length=4000, default='[]')

    def get_fundings_sum(self):
        try:
            funding_sum = 0
            fundings = list()
            for funding in Funding.objects.filter(tournament_name=self.tournament_name, confirm='yes'):
                fundings.append(funding)
                # print(funding.amount)
            for funding_amount in fundings:
                funding_sum = funding_sum + funding_amount.amount
            return funding_sum
        except ValueError:
            return '-'

    def get_fundings_percentage(self):
        try:
            funding_sum = 0
            fundings = list()
            for funding in Funding.objects.filter(tournament_name=self.tournament_name, confirm='yes'):
                fundings.append(funding)
            for funding_amount in fundings:
                funding_sum = funding_sum + funding_amount.amount
            funding_rate = funding_sum / int(self.funding_goal) * 100
            return funding_rate
        except ValueError:
            return '-'

            # d_day 연산
    def get_day(self):
        now = datetime.now()
        # print(self.starttime)
        try:
            end_time = datetime.strptime(self.tournament_starttime, '%Y/%m/%d %H:%M')
            d_day = str(-(end_time-now).days)
            if not d_day.startswith('-'):
                d_day = '+' + d_day
            return 'D'+d_day
        except ValueError:
            return 'D-X'

    def get_participation(self):
        participation_qs = list()
        for participation in Participation.objects.filter(tournament_name=self.tournament_name):
            participation_qs.append(participation)

        participation_num = len(participation_qs)
        return participation_num

    def get_funding_num(self):
        funding_qs = list()
        for funding in Funding.objects.filter(tournament_name=self.tournament_name, confirm='yes'):
            funding_qs.append(funding)

        funding_num = len(funding_qs)
        if funding_num == '':
            return 0
        return funding_num

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=200, default='')
    tournament_name = models.CharField(max_length=400, default='')
    video_name = models.CharField(max_length=400, default='')
    video_url = models.CharField(max_length=2000, default='')
    when = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))

class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=200, default='')
    tournament_name = models.CharField(max_length=400, default='')
    username = models.CharField(max_length=400, default='')
    dummy_username = models.CharField(max_length=400, default='')
    seed = models.CharField(max_length=200, default='')
    challonge_id = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')
    phone = models.CharField(max_length=200, default='')
    etc1 = models.CharField(max_length=400, default='-')
    etc2 = models.CharField(max_length=400, default='-')
    etc3 = models.CharField(max_length=2000, default='-')
    etc4 = models.CharField(max_length=400, default='-')
    etc5 = models.CharField(max_length=2000, default='-')
    input = models.CharField(max_length=2000, default='[]')
    when = models.CharField(max_length=400, default=timezone.localtime(timezone.now()))
    confirm = models.CharField(max_length=200, default='-')
    checkin = models.CharField(max_length=200, default='-')
    score = models.CharField(max_length=400, default='-')
    result = models.CharField(max_length=400, default='-')
    prize = models.CharField(max_length=400, default='-')

    def get_input_list(self):
        participation_input = ast.literal_eval(self.input)
        return participation_input

class Privacy(models.Model):
    id = models.AutoField(primary_key=True)
    content = summer_fields.SummernoteTextField()

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    content = summer_fields.SummernoteTextField()

class Help(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200, default='')
    question = models.CharField(max_length=1000, default='')
    answer = summer_fields.SummernoteTextField()

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=200, default='')
    tournament_name = models.CharField(max_length=400, default='')
    username = models.CharField(max_length=400, default='')
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    depth = models.IntegerField(default=0)
    path = models.CommaSeparatedIntegerField(max_length=4000)
    like = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=400, default='')
    user = models.ForeignKey(User)
    message = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message

class Gamerule(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_game = models.CharField(max_length=200, default='')
    tournament_type = models.CharField(max_length=200, default='')
    content = summer_fields.SummernoteTextField()

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    usage = models.CharField(max_length=200, default='')
    url = models.CharField(max_length=2000, default='')

class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=400, default='')
    email = models.CharField(max_length=400, default='')

class UploadFileModel(models.Model):
    file_tournament = models.FileField(upload_to='tournament', null=True, blank=True)
    file_profile = models.FileField(upload_to='profile', null=True, blank=True)