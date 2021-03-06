from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_gao.views.home', name='home'),
    # url(r'^web_gao/', include('web_gao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^index/$','blog.views.index'),
	url(r'^disp_goods/$','blog.views.disp_goods'),
	url(r'^regist/$','blog.views.regist_user'),
	url(r'^login/$','blog.views.login_user'),
	url(r'^logout/$','blog.views.logout_user'),
	url(r'^order/$','blog.views.order'),
	url(r'^pay/$','blog.views.pay'),
)
