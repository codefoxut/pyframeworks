# -*- coding: utf-8 -*-
from __future__ import unicode_literals


__all__ = ['index', 'detail', 'results', 'vote']

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % escape(question_id))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % escape(question_id))


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % escape(question_id))