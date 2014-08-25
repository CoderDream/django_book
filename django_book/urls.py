from django.conf.urls import patterns
from django.conf.urls import url

from django.contrib.auth.views import login
from django.contrib.auth.views import logout

#include, 

#from django_book.views import *
from django_book.views import hello
from django_book.views import current_datetime
from django_book.views import hours_ahead
from django_book.views import hello_base
from django_book.views import request_test
from django_book.views import show_image
from django_book.views import show_pdf
from django_book.views import show_cookie
from django_book.views import set_cookie
from django_book.views import del_cookie
from django_book.views import show_session
from django_book.views import set_session
from django_book.views import del_session
from django_book.views import welcome

from django_book.user.views import search_form
from django_book.user.views import search
from django_book.user.views import create_user
from django_book.user.views import user_list
from django_book.user.views import user_modify
from django_book.user.views import user_delete

from django_book.person.views import classroom_add
from django_book.person.views import classroom_list
from django_book.person.views import classroom_modify
from django_book.person.views import classroom_delete

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_book.views.home', name='home'),
    # url(r'^django_book/', include('django_book.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),  
    url(r'^^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^hello_base/$', hello_base),
    url(r'^request_test/$', request_test),
    url(r'^search_form/$', search_form),
    url(r'^search/$', search),
    url(r'^classroom/add/$', classroom_add),
    url(r'^classroom/list/$', classroom_list),
    url(r'^classroom/modify/(\d+)/$', classroom_modify),
    url(r'^classroom/delete/(\d+)/$', classroom_delete), 
    url(r'^show_image/$', show_image),
    url(r'^show_pdf/$', show_pdf),
    url(r'^test_cookie/show/$', show_cookie),
    url(r'^test_cookie/set/(\w+)/$', set_cookie),
    url(r'^test_cookie/del/$', del_cookie),
    url(r'^test_session/show/$', show_session),
    url(r'^test_session/set/(\w+)/$', set_session),
    url(r'^test_session/del/$', del_session),
    url(r'^accounts/login/$',  login, {'template_name': 'login.html'}),  
    url(r'^accounts/logout/$', logout), 
    url(r'^welcome/$', welcome),
    url(r'^user/add/$', create_user),
    url(r'^user/list/$', user_list),
    url(r'^user/modify/(\d+)/$', user_modify),
    url(r'^user/delete/(\d+)/$', user_delete),
)