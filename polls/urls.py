from django.conf.urls import include, url

from polls.views import raw_views, v1_views
from polls import views

app_name = 'polls'

raw_urlpatterns = [
    url(r'^$', raw_views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', raw_views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', raw_views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', raw_views.vote, name='vote'),
]

v1_urlpatterns = [
    url(r'^$', v1_views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', v1_views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



urlpatterns = [
    url(r'^raw/', include(raw_urlpatterns, namespace='raw')),
    url(r'^v1/', include(v1_urlpatterns, namespace='v1')),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]