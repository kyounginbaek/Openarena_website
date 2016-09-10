from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^looking/$', views.looking, name='looking'),
    url(r'^making/$', views.making, name='making'),
    url(r'^tournament_url_check/$', views.making, name='tournament_url_check'),
    url(r'^video/$', views.video, name='video'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^competition/$', views.competition, name='competition'),

    url(r'^contact/$', views.contact, name="contact"),
    url(r'^help/$', views.help, name="help"),
]