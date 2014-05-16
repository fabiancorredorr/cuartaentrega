from django.conf.urls import patterns, url

from appencuesta import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
     # ex: /appencuesta/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /appencuesta/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /appencuesta/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)