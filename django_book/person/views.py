# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, RequestContext
from django.db import connection, transaction
from django_book.person.models import Classroom

def classroom_add_post(request):
    if 'name' in request.GET and request.GET['name'] and 'tutor' in request.GET and request.GET['tutor']:
        name = request.GET['name']
        tutor = request.GET['tutor']

        # cursor=connection.cursor()
        # sql='insert into person_classroom (name,tutor) values (\''+name+'\',\''+tutor+'\')'
        # cursor.execute(sql)
        # transaction.commit_unless_managed()
        # cursor.close()

        c = Classroom(name=name, tutor=tutor)
        c.save()

        return render_to_response('person/classroom_add_result.html',
            {'name': name})
    else:
        return render_to_response('person/classroom_add.html', {'error': True})

def classroom_add(request):
    if request.POST.has_key('name') and request.POST.has_key('tutor') :
        name = request.POST['name']
        tutor = request.POST['tutor']
        c = Classroom(name=name, tutor=tutor)
        c.save()

        return render_to_response('person/classroom_add_result.html',
            {'name': name}, context_instance=RequestContext(request))
    else:
        return render_to_response('person/classroom_add.html', {'error': True}, context_instance=RequestContext(request))

def classroom_list(request):
    #cursor = connection.cursor()
    sql = 'select id, name, tutor from person_classroom'
    classroom_list = Classroom.objects.raw(sql)
    
    # classroom_list = Classroom.objects.all()
    return render_to_response('person/classroom_list.html',
        {'classroom_list': classroom_list})

def classroom_modify_backup(request, id1):
    cursor = connection.cursor()
    sql = 'select id,name,tutor from person_classroom where id=' + id1
    classroom_list = Classroom.objects.raw(sql)
    old_name = classroom_list[0].name
    old_tutor = classroom_list[0].tutor
    if 'name' in request.GET and request.GET['name'] and 'tutor' in request.GET and request.GET['tutor']:
        new_name = request.GET['name']
        new_tutor = request.GET['tutor']
        cursor = connection.cursor()
        sql = 'update person_classroom set name=\'' + new_name + '\',tutor=\'' + new_tutor + '\' where id=\'' + id1 + '\''
        cursor.execute(sql)
        transaction.commit_unless_managed()
        cursor.close()
        return render_to_response('person/classroom_modify_result.html',
            {'old_name': old_name, 'old_tutor':old_tutor, 'new_name':new_name, 'new_tutor':new_tutor})
    else:
        return render_to_response('person/classroom_modify.html', {'error': True, 'id':id1, 'name':old_name, 'tutor':old_tutor})

def classroom_modify_post(request, id1):
    cursor = connection.cursor()
    classroom = Classroom.objects.get(id=id1)
    old_name = classroom.name
    old_tutor = classroom.tutor
    cursor.close()
    if 'name' in request.GET and request.GET['name'] and 'tutor' in request.GET and request.GET['tutor']:
        new_name = request.GET['name']
        new_tutor = request.GET['tutor']
        classroom.name = new_name
        classroom.tutor = new_tutor
        classroom.save()
        return render_to_response('person/classroom_modify_result.html',
            {'old_name': old_name, 'old_tutor':old_tutor, 'new_name':new_name, 'new_tutor':new_tutor})
    else:
        return render_to_response('person/classroom_modify.html', {'error': True, 'id':id1, 'name':old_name, 'tutor':old_tutor})

def classroom_modify_backup_2(request, id1):
    cursor = connection.cursor()
    classroom = Classroom.objects.get(id=id1)
    old_name = classroom.name
    old_tutor = classroom.tutor
    cursor.close()

    if request.POST.has_key('name') and request.POST.has_key('tutor'):
        new_name = request.POST['name']
        new_tutor = request.POST['tutor']
        classroom.name = new_name
        classroom.tutor = new_tutor
        classroom.save()
        return render_to_response('person/classroom_modify_result.html',
            {'old_name': old_name, 'old_tutor':old_tutor, 'new_name':new_name, 'new_tutor':new_tutor}, context_instance=RequestContext(request))
    else:
        return render_to_response('person/classroom_modify.html', {'error': True, 'id':id1, 'name':old_name, 'tutor':old_tutor}, context_instance=RequestContext(request))

def classroom_modify(request, id1):
    GetHost = request.get_host()
    try:
        GetHTTP_REFERER = request.META['HTTP_REFERER']
    except KeyError:
        GetHTTP_REFERER = 'unknown'

    if GetHTTP_REFERER != 'unknown' and GetHTTP_REFERER.find(GetHost) > 0:
        cursor = connection.cursor()
        classroom = Classroom.objects.get(id=id1)
        old_name = classroom.name
        old_tutor = classroom.tutor
        cursor.close()
        if request.POST.has_key('name') and request.POST.has_key('tutor') :
            new_name = request.POST['name']
            new_tutor = request.POST['tutor']
            classroom.name = new_name
            classroom.tutor = new_tutor
            classroom.save()
            return render_to_response('person/classroom_modify_result.html',
                {'old_name': old_name, 'old_tutor':old_tutor, 'new_name':new_name, 'new_tutor':new_tutor}, context_instance=RequestContext(request))
        else:
            return render_to_response('person/classroom_modify.html', {'error': True, 'id':id1, 'name':old_name, 'tutor':old_tutor}, context_instance=RequestContext(request))
    else:
        return render_to_response('person/error.html')

def classroom_delete(request, id1):
    cursor = connection.cursor()
    classroom = Classroom.objects.get(id=id1)
    old_name = classroom.name
    classroom.delete()
    classroom_list = Classroom.objects.all()
    cursor.close()
    return render_to_response('person/classroom_delete_result.html', {'name':old_name})