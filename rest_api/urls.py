from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from rest_api.users_api.views import UserViewSet, GroupViewSet
from rest_api.snippets_api.views import SnippetViewSet, SnippetUserViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()

router.register(r'auth-users', UserViewSet)
router.register(r'auth-groups', GroupViewSet)
router.register(r'users', SnippetUserViewSet)
router.register(r'snippets', SnippetViewSet)



schema_view = get_schema_view(title='Pastebin API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^drf/', include('rest_api.snippets_api.urls')),
]
