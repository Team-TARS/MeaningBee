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
from MeaningBeeApp.models import Word,WordMeaning
from random import randint
from MeaningBeeApp.decorators import my_login_required

# View to fetch a random word and provide it to the player

@my_login_required
@csrf_exempt
def write_definitions(request):
	response_data = {}
	response_data['result'] = 'fail'
	if request.method == 'POST' and request.is_ajax():
		received_json_data=json.loads(request.body)
		print received_json_data['userDefinition']
		# TODO - INSERT INTO OTHER DBS
		response_data['result'] = 'success'
	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)