# -*- coding: utf-8 -*-
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>现在时间是 %s.</body></html>" % now
    return HttpResponse(html)