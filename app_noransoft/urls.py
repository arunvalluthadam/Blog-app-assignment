from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^$', 'app_noransoft.views.home', name='home'),
    url(r'^one-page/$', 'app_noransoft.views.one_page', name='one_page'),
    url(r'^add/$', 'app_noransoft.views.add', name='add'),
    url(r'^category/$', 'app_noransoft.views.category', name='category'),
)
