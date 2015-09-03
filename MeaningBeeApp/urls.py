from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views


urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^login/', views.login, name='login'),
     url(r'^create_post/', views.create_post, name='create_post'),
     url(r'^login_action/', views.login_action, name='login'),
     url(r'^register_action/', views.register_action, name='register'),
     url(r'^choice_screen/', views.choice, name='choice'),
     url(r'^player_dashboard/', views.dashboard, name='dashboard'),
     url(r'^loading/', views.loadgame, name='loadgame'),
     url(r'^begin_game/', views.all_loaded, name='all_loaded'),
     url(r'^objections/', views.pending_objections, name='pending_objections'),
     url(r'^registration/', views.registration, name='registration'),
)
 


