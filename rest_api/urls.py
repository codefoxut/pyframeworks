from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api import views
from rest_api.snippets import views as snippets_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

snippets_urls = [
    url(r'^snippets/$', snippets_views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippets_views.snippet_detail),
]

snippets_urls = format_suffix_patterns(snippets_urls)

urlpatterns += snippets_urls
