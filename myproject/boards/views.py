# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
# Home page
def home(request):
	return HttpResponse('Hello, World!')
