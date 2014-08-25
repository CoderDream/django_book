# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User

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

    
def create_user(request):
    if request.POST.has_key('username') and request.POST.has_key('password') and request.POST.has_key('email') :
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        user.save()
        return render_to_response('user/user_add_result.html',
            {'username': username},context_instance=RequestContext(request))
    else:
        return render_to_response('user/user_add.html', {'error': True},context_instance=RequestContext(request))

def user_list(request):
        user_list = User.objects.all()
        return render_to_response('user/user_list.html',
            {'user_list': user_list})

def user_delete(request,id1):
    GetHost = request.get_host()
    try:  
        GetHTTP_REFERER = request.META['HTTP_REFERER']  
    except KeyError:  
        GetHTTP_REFERER = 'unknown'
        
    if GetHTTP_REFERER!='unknown' and GetHTTP_REFERER.find(GetHost)>0:
        user = User.objects.get(id=id1)
        old_name = user.username
        user.delete()
        return render_to_response('user/user_delete_result.html',{'name':old_name})
    else:
        return render_to_response('user/error.html')


def user_modify(request,id1):
    GetHost = request.get_host()
    try:  
        GetHTTP_REFERER = request.META['HTTP_REFERER']  
    except KeyError:  
        GetHTTP_REFERER = 'unknown'
        
    if GetHTTP_REFERER!='unknown' and GetHTTP_REFERER.find(GetHost)>0:
        user = User.objects.get(id=id1)
        old_username = user.username
        old_email = user.email
        old_password = user.password
        if request.POST.has_key('username')  and request.POST.has_key('email') and request.POST.has_key('password') :
            new_username = request.POST['username']
            new_email = request.POST['email']
            new_password = request.POST['password']
            user.username = new_username
            user.email = new_email
            user.set_password(new_password)
            #Django 在 ``django.contrib.auth`` 提供了2个函数: ``authenticate()``和 ``login()`` 。
            #如果通过给定的用户名和密码做认证，请使用 ``authenticate()`` 函数。
            #user = authenticate(username=username,password=old_password)
            #自己修改密码时首先验证旧密码是否正确
            #user.password=new_password  #这样不行的
            user.save()
            return render_to_response('user/user_modify_result.html',
                {'old_username': old_username,'old_email':old_email,'old_password':old_password,'new_username': new_username,'new_email':new_email,'new_password':new_password},context_instance=RequestContext(request))
        else:
            return render_to_response('user/user_modify.html', {'error': True,'id':id1,'username':old_username,'email':old_email,'password':old_password},context_instance=RequestContext(request))
    else:
        return render_to_response('user/error.html') 