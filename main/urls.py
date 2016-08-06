from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^looking/$', views.looking, name='looking'),
    url(r'^making/$', views.making, name='making'),
    url(r'^making_submit/$', views.making_submit, name='making_submit'),
    url(r'^video/$', views.video, name='video'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^competition/$', views.competition, name='competition'),

    url(r'^mypage/$', views.mypage, name="mypage"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^help/$', views.help, name="help"),
]