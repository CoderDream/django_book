from django.conf.urls import patterns, url
#include, 

#from django_book.views import *
from django_book.views import hello, current_datetime, hours_ahead, hello_base

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
    
)