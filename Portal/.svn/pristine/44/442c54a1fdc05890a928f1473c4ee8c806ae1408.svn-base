__author__ = 'honglei.yu'
#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def showcode(request):
    return render_to_response('code.html', context_instance=RequestContext(request))
