from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api.snippets_api import views as snippets_views


urlpatterns = [
    url(r'^users/$', snippets_views.UserList.as_view(), name='snippet-user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', snippets_views.UserDetail.as_view(), name='user-detail'),

    url(r'^v4/$', snippets_views.SnippetListMixin.as_view()),
    url(r'^v4/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailMixin.as_view()),

    # version 3
    url(r'^v3/$', snippets_views.SnippetListAPIView.as_view()),
    url(r'^v3/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailAPIView.as_view()),
    # version 2
    url(r'^v2/$', snippets_views.snippet_list2),
    url(r'^v2/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail2),
    # version 1
    url(r'^v1/$', snippets_views.snippet_list1),
    url(r'^v1/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail1),

]

urlpatterns = format_suffix_patterns(urlpatterns)