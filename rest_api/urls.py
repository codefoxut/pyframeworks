from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views
from rest_api.snippets_api import views as snippets_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

snippets_urls = [
    url(r'^snippets/$', snippets_views.SnippetListGeneric.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailGeneric.as_view()),

    url(r'^snippets4/$', snippets_views.SnippetListMixin.as_view()),
    url(r'^snippets4/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailMixin.as_view()),

    # version 3
    url(r'^snippets3/$', snippets_views.SnippetList.as_view()),
    url(r'^snippets3/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetail.as_view()),
    # version 2
    url(r'^snippets2/$', snippets_views.snippet_list2),
    url(r'^snippets2/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail2),
    # version 1
    url(r'^snippets1/$', snippets_views.snippet_list1),
    url(r'^snippets1/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail1),
]

snippets_urls = format_suffix_patterns(snippets_urls)

urlpatterns += snippets_urls
