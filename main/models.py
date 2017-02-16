from django.utils import timezone
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django_summernote import fields as summer_fields

class Fundingdummy(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    amount = models.IntegerField(default=0)
    reward = models.CharField(max_length=100, default='-')
    comment = models.TextField(default='-')
    orderno = models.CharField(max_length=40, default='-')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))
    thanks = models.CharField(max_length=20, default='-')

class Funding(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    amount = models.IntegerField(default=0)
    reward = models.CharField(max_length=100, default='-')
    comment = models.TextField(default='-')
    orderno = models.CharField(max_length=40, default='-')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))
    thanks = models.CharField(max_length=20, default='-')

class Making(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))
    tournament_name = models.CharField(max_length=40, default='')
    tournament_game = models.CharField(max_length=20, default='')
    tournament_url = models.CharField(max_length=20, default='')
    streaming_url = models.CharField(max_length=20, default='')
    streaming_url_spec = models.CharField(max_length=40, default='')
    registration = models.CharField(max_length=20, default='')
    registration_team = models.CharField(max_length=20, default='')
    participant = models.CharField(max_length=20, default='')
    starttime = models.CharField(max_length=20, default='')
    checkin = models.CharField(max_length=20, default='')
    checkin_time = models.CharField(max_length=20, default='')
    description = summer_fields.SummernoteTextField()
    funding_goal = models.CharField(max_length=20, default='')
    promise = models.CharField(max_length=200, default='')
    promise_spec = models.CharField(max_length=200, default='')
    reward = models.CharField(max_length=200, default='')
    reward_spec = models.CharField(max_length=200, default='')
    template = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')
    confirm = models.CharField(max_length=20, default='')

    notice = summer_fields.SummernoteTextField()
    funding_endtime = models.CharField(max_length=20, default='')
    participation_endtime = models.CharField(max_length=20, default='')
    summary = models.TextField(default='')
    main_image = models.CharField(max_length=100, default='')
    cover_image = models.CharField(max_length=100, default='')
    poster_image = models.CharField(max_length=100, default='')
    match_image = models.CharField(max_length=100, default='')

class Tournament(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    created = models.DateTimeField(auto_now_add=True)
    #tab1
    tournament_name = models.CharField(max_length=40, default='')
    tournament_game = models.CharField(max_length=40, default='')
    tournament_game_etc = models.CharField(max_length=40, default='')
    tournament_image = models.CharField(max_length=200, default='')
    tournament_summary = summer_fields.SummernoteTextField()
    tournament_url = models.CharField(max_length=40, default='')
    #tab2
    tournament_starttime = models.CharField(max_length=20, default='')
    tournament_endtime = models.CharField(max_length=20, default='')
    #tournament_format = ?
    tournament_rule = summer_fields.SummernoteTextField()
    registration = models.CharField(max_length=20, default='') #yes or no
    #if tournament_registration = yes
    registration_type = models.CharField(max_length=20, default='') #individual or team
    participation_template = models.CharField(max_length=200, default='')
    participation_number = models.CharField(max_length=20, default='')
    participation_time = models.CharField(max_length=20, default='') #default or custom
    #if participation_time = custom
    participation_starttime = models.CharField(max_length=20, default='')
    participation_endtime = models.CharField(max_length=20, default='')
    participation_checkin = models.CharField(max_length=20, default='') #yes or no
    #if participation_checkin = yes
    participation_checkin_time = models.CharField(max_length=20, default='')
    #tab3
    funding_info = models.CharField(max_length=20, default='') #only yes
    participation_fee = models.CharField(max_length=20, default='') #yes or no
    # if participation_fee = yes
    participation_fee_number = models.CharField(max_length=20, default='')
    funding = models.CharField(max_length=20, default='') #yes or no
    # if funding = yes
    funding_goal = models.CharField(max_length=20, default='')
    funding_time = models.CharField(max_length=20, default='') #default or custom
    # if funding_time = custom
    funding_starttime = models.CharField(max_length=20, default='')
    funding_endtime = models.CharField(max_length=20, default='')
    reward = models.CharField(max_length=20, default='') #yes or no
    #if reward = yes
    reward_number = models.CharField(max_length=20, default='')
    reward_spec = models.CharField(max_length=200, default='')
    promise = models.CharField(max_length=20, default='') #yes or no
    #if promise = yes
    promise_number = models.CharField(max_length=20, default='')
    promise_spec = models.CharField(max_length=200, default='')
    funding_notice = models.CharField(max_length=20, default='') #yes
    #tab4
    profile_image = models.CharField(max_length=200, default='')
    profile_name_question = models.CharField(max_length=20, default='') #default or custom
    profile_name = models.CharField(max_length=40, default='')
    profile_introduction = summer_fields.SummernoteTextField()
    streaming_site = models.CharField(max_length=200, default='')
    streaming_url = models.CharField(max_length=400, default='')
    profile_email_question = models.CharField(max_length=20, default='')  # default or custom
    profile_email = models.CharField(max_length=40, default='')
    profile_phone = models.CharField(max_length=20, default='')
    creator_enrollment = models.CharField(max_length=20, default='')
    #after submit
    confirm = models.CharField(max_length=20, default='') #yes or no(reviewing)
    #template
    cover_image = models.CharField(max_length=200, default='')
    logo_image = models.CharField(max_length=200, default='')

class Video(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    video_name = models.CharField(max_length=40, default='')
    video_url = models.CharField(max_length=200, default='')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))

class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    name = models.CharField(max_length=40, default='')
    teamname = models.CharField(max_length=40, default='-')
    teammember = models.CharField(max_length=200, default='-')
    email = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')
    etc1 = models.CharField(max_length=40, default='-')
    etc2 = models.CharField(max_length=40, default='-')
    etc3 = models.CharField(max_length=40, default='-')
    etc4 = models.CharField(max_length=40, default='-')
    etc5 = models.CharField(max_length=200, default='-')
    etc6 = models.CharField(max_length=200, default='-')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))
    confirm = models.CharField(max_length=20, default='-')
    checkin = models.CharField(max_length=20, default='-')
    score = models.CharField(max_length=40, default='-')
    result = models.CharField(max_length=40, default='-')
    prize = models.CharField(max_length=40, default='-')

class Privacy(models.Model):
    id = models.AutoField(primary_key=True)
    content = summer_fields.SummernoteTextField()

class Agreement(models.Model):
    id = models.AutoField(primary_key=True)
    content = summer_fields.SummernoteTextField()

class Help(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, default='')
    question = models.CharField(max_length=100, default='')
    answer = summer_fields.SummernoteTextField()

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    content = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    depth = models.IntegerField(default=0)
    path = models.CommaSeparatedIntegerField(max_length=400)
    like = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=40, default='')
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message

class Gamerule(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_game = models.CharField(max_length=20, default='')
    tournament_type = models.CharField(max_length=20, default='')
    content = summer_fields.SummernoteTextField()

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    usage = models.CharField(max_length=20, default='')
    url = models.CharField(max_length=200, default='')

class Userinfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')