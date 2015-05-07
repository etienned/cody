# -*- coding: utf-8 -*-

from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from voiture import views


urlpatterns = [
    url(r'^voiture/$', views.VoitureList.as_view(), name='list'),
    url(r'^voiture/(?P<pk>[0-9]+)/$', views.VoitureDetail.as_view(), name='detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
