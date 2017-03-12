from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^tournaments/$', views.tournaments, name='tournaments'),
    url(r'^clubs/$', views.clubs, name='clubs'),
    url(r'^making/$', views.making, name='making'),
    url(r'^tournament_url_check/$', views.making, name='tournament_url_check'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^migal/$', views.migal, name='migal'),
    url(r'^whyachi/$', views.whyachi, name='whyachi'),
    url(r'^macho/$', views.macho, name='macho'),
    url(r'^macho2/$', views.macho2, name='macho2'),
    url(r'^scc2/$', views.scc2, name='scc2'),
    url(r'^vsc/$', views.vsc, name='vsc'),
    url(r'^ringoncup/$', views.ringoncup, name='ringoncup'),
    url(r'^scc3/$', views.scc3, name='scc3'),
    url(r'^chainkiller_s1/$', views.chainkiller_s1, name='chainkiller_s1'),
    url(r'^vsc2/$', views.vsc2, name='vsc2'),
    url(r'^moon/$', views.moon, name='moon'),

    url(r'^contact/$', views.contact, name="contact"),
    url(r'^help/$', views.help, name="help"),
    url(r'^privacy/$', views.privacy, name="privacy"),
    url(r'^agreement/$', views.agreement, name="agreement"),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^create/$', views.create, name='create'),
    url(r'^template/$', views.template, name='template'),
    url(r'^test/$', views.test, name='test'),
    url(r'^members/$', views.members, name='members'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)