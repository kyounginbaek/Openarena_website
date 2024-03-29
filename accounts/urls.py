from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^mypage/$', views.mypage, name="mypage"),
    url(r'^withdrawal/$', views.withdrawal, name="withdrawal"),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
