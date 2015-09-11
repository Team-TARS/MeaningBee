from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import json 

# View for login authentication checking
# username and password are sent through ajax calls 
# verified if they exist
@csrf_exempt
def login_action(request):  
    response_data = {}
    response_data['result'] = 'fail' 
    print request.body   
    if request.method == 'POST' and request.is_ajax():
        received_json_data=json.loads(request.body)
        # the json data that is sent from the front end 
        print received_json_data
        # extract the username from the json data
        username = received_json_data['username']
        # extract the password from the json data 
        password = received_json_data['password']
        # authenticate the user and password                                                                                           
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