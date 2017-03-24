from django.conf.urls import url
from django.http import HttpResponse
from . import views
from .feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^feed/$', LatestEntriesFeed()),
    url(r'^page/(?P<pk>[0-9]+)/$', views.page_detail, name='page_detail'),
    url(r'^page/(?P<pk>[0-9]+)/edit/$', views.page_edit, name='page_edit'),
    url(r'^page/new/$', views.page_new, name='page_new'),
    url(r'^comments/$', views.new_comments_list, name='new_comments_list'),
    url(r'^clist/(?P<pk>[0-9]+)/approve/$', views.comment_approve_list, name='comment_approve_list'),
    url(r'^clist/(?P<pk>[0-9]+)/remove/$', views.comment_remove_list, name='comment_remove_list'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", content_type="text/plain")),
]