from django.conf.urls import url

from rest_api.simple_api import views as simple_views

urlpatterns = [

    url(r'^$', simple_views.api_root),
    url(r'^hello/$', simple_views.hello_world,
        name='simple-hello'),
    url(r'^list/$', simple_views.simple_list,
        name='simple-list'),
]
