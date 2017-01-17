from django.utils import timezone
from django.db import models
from django_summernote import fields as summer_fields
from django import forms
from django.contrib.auth.models import User

class Fundingdummy(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    amount = models.IntegerField(default=0)
    comment = models.TextField(max_length=200, default='')
    orderno = models.CharField(max_length=40, default='')
    when = models.CharField(max_length=40, default=timezone.localtime(timezone.now()))

class Funding(models.Model):
    id = models.AutoField(primary_key=True)
    tournament_id = models.CharField(max_length=20, default='')
    tournament_name = models.CharField(max_length=40, default='')
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    amount = models.IntegerField(default=0)
    reward = models.CharField(max_length=100, default='-')
    comment = models.TextField(max_length=200, default='-')
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
    description = summer_fields.SummernoteTextField(default='')
    funding_goal = models.CharField(max_length=20, default='')
    promise = models.CharField(max_length=200, default='')
    promise_spec = models.CharField(max_length=200, default='')
    reward = models.CharField(max_length=200, default='')
    reward_spec = models.CharField(max_length=200, default='')
    template = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')
    confirm = models.CharField(max_length=20, default='')

    notice = summer_fields.SummernoteTextField(default='')
    funding_endtime = models.CharField(max_length=20, default='')
    participation_endtime = models.CharField(max_length=20, default='')
    summary = models.TextField(max_length=400, default='')
    main_image = models.CharField(max_length=100, default='')
    cover_image = models.CharField(max_length=100, default='')
    poster_image = models.CharField(max_length=100, default='')
    match_image = models.CharField(max_length=100, default='')

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
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    depth = models.IntegerField(default=0)
    path = models.CommaSeparatedIntegerField(max_length=400)

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