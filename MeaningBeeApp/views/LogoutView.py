from django.contrib.auth import logout
from django.shortcuts import render

def logout_action(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'login_page.html')