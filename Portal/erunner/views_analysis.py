__author__ = 'honglei.yu'
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def analysis(request):
    return render_to_response('analysis.html', context_instance=RequestContext(request))
