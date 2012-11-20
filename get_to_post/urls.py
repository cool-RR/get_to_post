# Copyright 2009-2012 Ram Rachum.
# This program is distributed under the MIT license.

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.GetToPostView.as_view()),
)
