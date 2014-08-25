# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

def search_form(request):
    return render_to_response('user/search_form.html')

# 这里有过个小问题，后台取到的值是u'x'结构，所以不会走到else中去。
def search_backup(request):  
    if 'q' in request.GET and request.GET['q']:  
        message = '您搜索的关键字是: %r' % request.GET['q']  
    else:  
        message = '请输入您要检索的内容'  
    return HttpResponse(message)

def search(request):  
    if 'q' in request.GET and request.GET['q']:  
        q = request.GET['q']  
        return render_to_response('user/search_result.html',  
            {'query': q})  
    else:  
        return render_to_response('user/search_form.html', {'error': True})    