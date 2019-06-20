""" Urls definitioins for the queue app
"""
from django.conf.urls import url
from . import views


app_name = 'socketdraw'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]