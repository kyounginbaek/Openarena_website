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

    def __str__(self):
        return self.username

class Tournament(models.Model):
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
    funding = models.CharField(max_length=20, default='')
    promise = models.CharField(max_length=400, default='')
    reward = models.CharField(max_length=400, default='')
    template = models.CharField(max_length=40, default='')
    phone = models.CharField(max_length=20, default='')
    letsmake = models.CharField(max_length=20, default='no')

    def __str__(self):
        return self.tournament_name