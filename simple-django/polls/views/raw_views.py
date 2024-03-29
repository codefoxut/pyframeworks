# -*- coding: utf-8 -*-
from __future__ import unicode_literals


__all__ = ['index', 'detail', 'results', 'vote']

from django.shortcuts import render
from django.http import HttpResponse
import html

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % html.escape(question_id))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % html.escape(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % html.escape(question_id))
