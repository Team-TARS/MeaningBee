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

@csrf_exempt
def register_action(request):
    response_data = {}
    response_data['result'] = 'fail' 
    print request.body
    if request.method == 'POST' and request.is_ajax():
        received_json_data=json.loads(request.body)
        print received_json_data
        first_name = received_json_data['firstname']
        last_name = received_json_data['lastname']
        date_of_birth = received_json_data['dateofbirth']
        user_name = received_json_data['username'] 
        password = received_json_data['password']                                                                                           
        response_data = {}
        try:
            userobj = User.objects.get(username=user_name)
            response_data['result'] = 'user exists' 
        
        except User.DoesNotExist:        
            user, created = User.objects.get_or_create(username=user_name)
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            print (user.first_name)
            strp_time = time.strptime(date_of_birth, "%m/%d/%Y")
            date_django = datetime.fromtimestamp(time.mktime(strp_time))

            # Always have var,created while using get_or_create  - important
            user_type, created = UserType.objects.get_or_create(usertype_name=UserType.PLAYER)

            #print(d.usertype_name)
            #user_type.get_usertype_name_display()
            user_details = UserProfile.objects.get_or_create(user=user,date_of_birth=date_django,usertype=user_type)    
            response_data['result'] = 'success' 
    
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

@csrf_exempt
def login_action(request):  
    response_data = {}
    response_data['result'] = 'fail' 
    print request.body   
    if request.method == 'POST' and request.is_ajax():
        received_json_data=json.loads(request.body)
        print received_json_data
        username = received_json_data['username'] 
        password = received_json_data['password']                                                                                           
        if request.method == 'POST':                                                                                                            
            request.session.set_test_cookie()                                                                                                     
            user =  authenticate(username=username, password=password)
            print user
            if user is not None:                                         
                response_data['result'] = 'success'
    print json.dumps(response_data)
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )

# @csrf_exempt
# def create_post(request):
#     print request.body
#     if request.method == 'POST' and request.is_ajax():
#         received_json_data=json.loads(request.body)
#         print received_json_data
#         username = received_json_data['username'] 
#         password = received_json_data['password']   
#         response_data = {}
#         feedback = Feedback(username=username, password=password, date=datetime.now())
#         feedback.save()
        
#         response_data['result'] = 'Create post successful!'
#         response_data['text'] = username


#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )