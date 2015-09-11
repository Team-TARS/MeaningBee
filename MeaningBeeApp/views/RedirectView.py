from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from MeaningBeeApp.models import UserProfile,UserType
import json 
import time
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html');

def login(request):
    return render(request, 'login_page.html');

def registration(request):
    return render(request,'registration_page.html');

def choice(request):
    return render(request, 'user_choice_screen.html');

def dashboard(request):
    return render(request, 'player_dashboard.html');

def loadgame(request):
    return render(request, 'load_game.html');

def all_loaded(request):
    return render(request, 'all_loaded.html');

def pending_objections(request):
    return render(request, 'pending_objection.html');