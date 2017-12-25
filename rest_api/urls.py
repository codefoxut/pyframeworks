from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api.users_api import views
from rest_api.snippets_api import views as snippets_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^snippets/', include('rest_api.snippets_api.urls')),
]

snippets_urls = [
    url(r'^$', snippets_views.api_root),
    url(r'^snippets/$', snippets_views.SnippetList.as_view(), name='snippets-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippets_views.SnippetDetail.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippets_views.SnippetHighlight.as_view()),
    url(r'^users/$', snippets_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', snippets_views.UserDetail.as_view()),

]

snippets_urls = format_suffix_patterns(snippets_urls)

urlpatterns += snippets_urls
