# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'blog2/index.html',{'name':'waking yang'})

def students(request):
	return render(request,'blog2/students.html',{'count':45})
