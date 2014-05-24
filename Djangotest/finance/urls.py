__author__ = 'cobalt'
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
                        url(r'$', 'finance.views.index', name='index'),
                       )