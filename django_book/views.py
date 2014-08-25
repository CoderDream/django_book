# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response

from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello World!")

def current_datetime_backup(request):
    now = datetime.datetime.now()
    html = "<html><body>现在时间是 %s。</body></html>" % now
    return HttpResponse(html)

def current_datetime_backup_2(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())

def hours_ahead_backup(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>再过 %s 个小时，时间将会是 %s。</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    author="CoderDream"
    return render_to_response('template_include.html', locals())

def hello_base(request):  
    MyString = 'Hello World'  
    return render_to_response('hello_base.html', locals())  