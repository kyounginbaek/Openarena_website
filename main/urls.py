from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^looking/$', views.looking, name='looking'),
    url(r'^making/$', views.making, name='making'),
    url(r'^tournament_url_check/$', views.making, name='tournament_url_check'),
    url(r'^video/$', views.video, name='video'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^migal/$', views.migal, name='migal'),
    url(r'^darkhumor/$', views.darkhumor, name='darkhumor'),
    url(r'^arch/$', views.arch, name='arch'),
    url(r'^macho/$', views.macho, name='macho'),

    url(r'^participation/$', views.participation, name='participation'),
    url(r'^reply/$', views.reply, name='reply'),
    url(r'^contents/$', views.contents, name='contents'),

    url(r'^contact/$', views.contact, name="contact"),
    url(r'^help/$', views.help, name="help"),
    url(r'^funding/$', views.funding, name="funding"),
    url(r'^privacy/$', views.privacy, name="privacy"),
    url(r'^agreement/$', views.agreement, name="agreement"),
]