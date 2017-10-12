# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import importlib
from django.utils import timezone
from django.views import generic

from polls.models import Question
from polls.views import raw_views, v1_views


# Create your views here.
def index(request):
    mode = request.GET.get('version', 'v1')
    mode_views = ".%s_views" % mode
    views_module = importlib.import_module(mode_views, 'polls.views')
    return views_module.index(request)


def detail(request, question_id):
    mode = request.GET.get('version', 'v1')
    mode_views = ".%s_views" % mode
    views_module = importlib.import_module(mode_views, 'polls.views')
    return views_module.detail(request, question_id)


def results(request, question_id):
    mode = request.GET.get('version', 'v1')
    mode_views = ".%s_views" % mode
    views_module = importlib.import_module(mode_views, 'polls.views')
    return views_module.results(request, question_id)


def vote(request, question_id):
    mode = request.GET.get('version', 'v1')
    mode_views = ".%s_views" % mode
    views_module = importlib.import_module(mode_views, 'polls.views')
    return views_module.vote(request, question_id)


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset_old(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    def get(self, request, *args, **kwargs):
        mode = request.GET.get('version')
        if request.GET and mode and mode in ['raw', 'v1']:
            resp = index(request)
        else:
            resp = super(IndexView, self).get(request)
        return resp


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, *args, **kwargs):
        mode = request.GET.get('version')
        if request.GET and mode and (mode in ['raw', 'v1']):
            resp = detail(request, args[0])
        else:
            resp = super(DetailView, self).get(request, *args, **kwargs)
        return resp


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get(self, request, *args, **kwargs):
        mode = request.GET.get('version')
        if request.GET and mode and (mode in ['raw', 'v1']):
            resp = results(request, args[0])
        else:
            resp = super(ResultsView, self).get(request, *args, **kwargs)
        return resp