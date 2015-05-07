from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    url(r'^$', 'app_noransoft.views.home', name='home'),
    url(r'^one-page/(?P<blog_id>\d+)$', 'app_noransoft.views.one_page', name='one_page'),
    url(r'^add/$', 'app_noransoft.views.add', name='add'),
    url(r'^category/$', 'app_noransoft.views.category', name='category'),
    url(r'^category-index/(?P<cat_name>\w+)$', 'app_noransoft.views.category_index', name='category_index'),
)
