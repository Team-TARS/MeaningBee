from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from MeaningBeeApp.views import LoginView
from MeaningBeeApp.views import RedirectView
from MeaningBeeApp.views import RegisterView
from MeaningBeeApp.views import FetchWordView
from MeaningBeeApp.views import LogoutView
from MeaningBeeApp.views import WriteUserDefinitionsView

urlpatterns = patterns('',
     url(r'^$', RedirectView.index, name='index'),
     url(r'^login/', RedirectView.login, name='login'),
     #url(r'^invalid_login/', RedirectView.invalid_login, name='invalid_login'),
     # url(r'^create_post/', views.create_post, name='create_post'),
     url(r'^write_user_definition/', WriteUserDefinitionsView.write_definitions, name='write_user_definition'),
     url(r'^login_action/', LoginView.login_action, name='login'),
     url(r'^logout/', LogoutView.logout_action, name='logout'),
     url(r'^register_action/', RegisterView.register_action, name='register'),
     url(r'^user_definitions/', RedirectView.user_definitions, name='user_definitions'),
     url(r'^choice_screen/', RedirectView.choice, name='choice'),
     url(r'^player_dashboard/', RedirectView.dashboard, name='dashboard'),
     url(r'^loading/', RedirectView.loadgame, name='loadgame'),
     url(r'^begin_game/', RedirectView.all_loaded, name='all_loaded'),
     url(r'^objections/', RedirectView.pending_objections, name='pending_objections'),
     url(r'^registration/', RedirectView.registration, name='registration'),
     url(r'^fetch_word/', FetchWordView.fetch_random_word, name='fetch_word'),
     
)
 


