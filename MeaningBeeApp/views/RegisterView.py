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

# View for registering users
# Once the data is all obtained from front end (post validation)
# UserProfile - Custom user with DOB and Type fields added to User
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
            response_data['result'] = 'user exists' #User with the same name exists
        
        except User.DoesNotExist:        
            user, created = User.objects.get_or_create(username=user_name)
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.save() #Save it in the user table first
            print (user.first_name)
            strp_time = time.strptime(date_of_birth, "%m/%d/%Y")
            date_django = datetime.fromtimestamp(time.mktime(strp_time)) 
            #Fetch DOB and convert it into Django DateTimeField

            # Always have var,created while using get_or_create  - important
            user_type, created = UserType.objects.get_or_create(usertype_name=UserType.PLAYER)
            # For the first run of the app - This must create the entry 'PLAYER' in the DB

            #print(d.usertype_name)
            #user_type.get_usertype_name_display()
            user_details = UserProfile.objects.get_or_create(user=user,date_of_birth=date_django,usertype=user_type)    
            response_data['result'] = 'success' 
    
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )