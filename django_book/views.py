# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from reportlab.pdfgen import canvas

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
sys.setdefaultencoding(default_encoding)

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

def request_test(request):
    GetPath = request.path
    GetHost = request.get_host()
    GetFullPath = request.get_full_path()
    GetIsSecure = request.is_secure()

    try:
        GetHTTP_REFERER = request.META['HTTP_REFERER']
    except KeyError:
        GetHTTP_REFERER = 'unknown'

    try:
        GetHTTP_USER_AGENT = request.META['HTTP_USER_AGENT']
    except KeyError:
        GetHTTP_USER_AGENT = 'unknown'

    try:
        GetREMOTE_ADDR = request.META['REMOTE_ADDR']
    except KeyError:
        GetREMOTE_ADDR = 'unknown'
    return render_to_response('request_test.html', locals())

def show_image(request):
    image_data = open("django_book/images/babyking.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")



def show_pdf(request):
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    pdfmetrics.registerFont(TTFont('SimHei','simhei.ttf'))

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 750, "Hello world.")
    p.setFont('SimHei', 12)
    p.drawString(100, 750, "你好，世界！")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response