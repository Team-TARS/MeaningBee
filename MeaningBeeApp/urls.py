from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^login/', views.login, name='login'),
     url(r'^choice_screen/', views.choice, name='choice'),
)
