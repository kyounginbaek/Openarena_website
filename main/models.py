from django.utils import timezone
from django.db import models

class Funding(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    orderno = models.CharField(max_length=40, default='')
    amount = models.CharField(max_length=40, default='')
    when = models.CharField(max_length=40, default=timezone.now())

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Making(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=40, default='')
    email = models.CharField(max_length=40, default='')
    when = models.CharField(max_length=40, default=timezone.now())
    tournament_name = models.CharField(max_length=40, default='')
    tournament_game = models.CharField(max_length=20, default='')
    tournament_url = models.CharField(max_length=20, default='')
    streaming_url = models.CharField(max_length=20, default='')
    streaming_url_spec = models.CharField(max_length=20, default='')
    registration = models.CharField(max_length=20, default='')
    registration_team = models.CharField(max_length=20, default='')
    participant = models.CharField(max_length=20, default='')
    starttime = models.CharField(max_length=20, default='')
    checkin = models.CharField(max_length=20, default='')
    checkin_time = models.CharField(max_length=20, default='')
    description = models.TextField(max_length=2000, default='')
    funding_goal = models.CharField(max_length=20, default='')
    promise = models.CharField(max_length=200, default='')
    promise_spec = models.CharField(max_length=200, default='')
    reward = models.CharField(max_length=200, default='')
    reward_spec = models.CharField(max_length=200, default='')
    template = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')
    confirm = models.CharField(max_length=20, default='no')

    main_image = models.CharField(max_length=100, default='')
    summary = models.CharField(max_length=100, default='')
    funder = models.CharField(max_length=20, default='')
    funding_now = models.CharField(max_length=20, default='')
    endtime = models.CharField(max_length=20, default='')
    cover_image = models.CharField(max_length=100, default='')
    poster_image = models.CharField(max_length=100, default='')
    match_image = models.CharField(max_length=100, default='')