from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='homepage'),
    url(r'^topics/$', views.list_topics, name="topics"),
    url(r'^topics/(?P<topic_title>.+)/$', views.post_topic, name="post"),
]