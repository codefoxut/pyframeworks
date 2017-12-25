from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from rest_api.snippets import views as snippets_views


urlpatterns = [
    url(r'', snippets_views.snippet_list),
    url(r'^(?P<pk>[0-9]+)/$', snippets_views.snippet_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)