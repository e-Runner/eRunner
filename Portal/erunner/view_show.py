__author__ = 'honglei.yu'
#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def showlog(request):
    return render_to_response('log.html', context_instance=RequestContext(request))
