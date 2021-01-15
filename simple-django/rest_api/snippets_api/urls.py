from django.conf.urls import url, include
from rest_framework import renderers
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api.snippets_api import views as snippets_views
from rest_api.snippets_api.views import SnippetViewSet, SnippetUserViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', SnippetUserViewSet)
router.register(r'snippets', SnippetViewSet)


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = SnippetUserViewSet.as_view({
    'get': 'list'
})
user_detail = SnippetUserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^v6/$', snippets_views.api_root),
    url(r'^snippets/v6/$', snippet_list,
        # name='snippet-list'
        ),
    url(r'^snippets/v6/(?P<pk>[0-9]+)/$', snippet_detail,
        # name='snippet-detail'
        ),
    url(r'^snippets/v6/(?P<pk>[0-9]+)/highlight/$', snippet_highlight,
        # name='snippet-highlight'
        ),
    url(r'^users/v2/$', user_list,
        name='snippet-user-list'
        ),
    url(r'^users/v2/(?P<pk>[0-9]+)/$', user_detail,
        # name='user-detail'
        ),

]

urlpatterns += [
url(r'^snippets/v5/$',
        snippets_views.SnippetList.as_view()),
    url(r'^snippets/v5/(?P<pk>[0-9]+)/$',
        snippets_views.SnippetDetail.as_view()),
    url(r'^snippets/v5/(?P<pk>[0-9]+)/highlight/$',
        snippets_views.SnippetHighlight.as_view()),
    url(r'^users/v1/$', snippets_views.UserList.as_view(), ),
    url(r'^users/v1/(?P<pk>[0-9]+)/$', snippets_views.UserDetail.as_view()),

    url(r'^snippets/v4/$', snippets_views.SnippetListMixin.as_view()),
    url(r'^snippets/v4/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailMixin.as_view()),

    # version 3
    url(r'^snippets/v3/$', snippets_views.SnippetListAPIView.as_view()),
    url(r'^snippets/v3/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetailAPIView.as_view()),
    # version 2
    url(r'^snippets/v2/$', snippets_views.snippet_list2),
    url(r'^snippets/v2/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail2),
    # version 1
    url(r'^snippets/v1/$', snippets_views.snippet_list1),
    url(r'^snippets/v1/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail1),

]

urlpatterns = format_suffix_patterns(urlpatterns)


urlpatterns += [
    url(r'^', include(router.urls)),
]