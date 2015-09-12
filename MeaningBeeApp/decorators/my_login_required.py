from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.contrib.auth.models import User
from MeaningBeeApp.models import UserProfile,UserType

def my_login_required(function):
	def wrapper(request,*args,**kw):
		if not request.user.is_authenticated():
			return render(request,'login_error.html')
		else:
			return function(request,*args,**kw)
	return wrapper
		