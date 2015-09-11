from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
import json 

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