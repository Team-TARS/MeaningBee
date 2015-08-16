from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def choice(request):
    return render(request, 'user_choice_screen.html')

def dashboard(request):
    return render(request, 'player_dashboard.html')

def loadgame(request):
    return render(request, 'load_game.html')

def all_loaded(request):
    return render(request,'all_loaded.html');

def pending_objections(request):
    return render(request,'pending_objection.html')