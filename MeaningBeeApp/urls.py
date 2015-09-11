from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from MeaningBeeApp.views import LoginView
from MeaningBeeApp.views import RedirectView
from MeaningBeeApp.views import RegisterView


urlpatterns = patterns('',
     url(r'^$', RedirectView.index, name='index'),
     url(r'^login/', RedirectView.login, name='login'),
     # url(r'^create_post/', views.create_post, name='create_post'),
     url(r'^login_action/', LoginView.login_action, name='login'),
     url(r'^register_action/', RegisterView.register_action, name='register'),
     url(r'^choice_screen/', RedirectView.choice, name='choice'),
     url(r'^player_dashboard/', RedirectView.dashboard, name='dashboard'),
     url(r'^loading/', RedirectView.loadgame, name='loadgame'),
     url(r'^begin_game/', RedirectView.all_loaded, name='all_loaded'),
     url(r'^objections/', RedirectView.pending_objections, name='pending_objections'),
     url(r'^registration/', RedirectView.registration, name='registration'),
)
 


