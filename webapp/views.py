# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from webapp.models import Counter


@api_view(['GET'])
def home(request):
        return render(request, 'index.epy', {'count' : Counter.Get().count})

@api_view(['POST'])
def increment(request):
        Counter.Increment()
        # OK
        return HttpResponse(status=200)
