#coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def login_view(request):
    errors = []
    if request.POST.has_key('Username') and request.POST.has_key('Password'):
        username = request.POST['Username']
        password = request.POST['Password']
        if not username:
            errors.append('Please enter a username.')
        elif len(username) < 3 or len(username) > 30:
            errors.append('Username length is between 3 and 30 chars.')
        elif not password:
            errors.append('Please enter a password.')
        elif len(password) < 3 or len(password) > 16:
            errors.append('Password length is between 3 and 16 chars.')
        else:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/mainframe/')
                else:
                    errors.append('The user has been disabled.')
            else:
                errors.append('Incorrect username or incorrect password.')
    return render_to_response("login.html",{'errors': errors})

def logout_view(request):
    logout(request)
    return render_to_response("login.html",{})
