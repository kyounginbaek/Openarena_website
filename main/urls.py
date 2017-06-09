from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # main_url
    url(r'^$', views.home, name='home'),
    url(r'^tournaments/$', views.tournaments, name='tournaments'),
    url(r'^tournaments_ct/$', views.tournaments_ct, name='tournaments_ct'),
    url(r'^t/(?P<url>[\w\-]+)/$', views.t, name='t'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^clubs/$', views.clubs, name='clubs'),
    url(r'^making/$', views.making, name='making'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^help/$', views.help, name="help"),
    url(r'^privacy/$', views.privacy, name="privacy"),
    url(r'^agreement/$', views.agreement, name="agreement"),
    url(r'^chat/$', views.chat, name='chat'),
    url(r'^create/$', views.create, name='create'),
    url(r'^members/$', views.members, name='members'),
    url(r'^funding_success/$', views.funding_success, name='funding_success'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)