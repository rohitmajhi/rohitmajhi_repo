# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('getid.views',
    (r'^thanks/$', 'thanks'),
    (r'^survey_thanks/$', 'survey_thanks'),
    (r'^out_there_now/$', 'get_interested_email'),
)