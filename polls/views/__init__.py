# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from polls.views import raw_views, v1_views

# Create your views here.
def index(request):
    if request.GET.get('version', '') == 'raw':
        resp = raw_views.index(request)
    else:
        resp = v1_views.index(request)

    return resp


def detail(request, question_id):
    if request.GET.get('version', '') == 'raw':
        resp = raw_views.detail(request, question_id)
    else:
        resp = v1_views.detail(request, question_id)
    return resp


def results(request, question_id):
    return raw_views.results(request, question_id)


def vote(request, question_id):
    return raw_views.vote(request, question_id)