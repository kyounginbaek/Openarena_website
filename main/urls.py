from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^looking/$', views.looking, name='looking'),
    url(r'^making/$', views.making, name='making'),
    url(r'^video/$', views.video, name='video'),
    url(r'^hallfame/$', views.hallfame, name='hallfame'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_page, name="logout_page"),
]