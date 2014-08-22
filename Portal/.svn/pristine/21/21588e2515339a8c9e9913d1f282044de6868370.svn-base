#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from erunner.models_dimension import ModVersion
from erunner.models_dimension import Modl
from erunner.models_dimension import RunSuite
from erunner.models_dimension import TestSuite
from django.http import HttpResponse

import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def configure(request):
    return render_to_response('configure.html', context_instance=RequestContext(request))


def AddRunSuite(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        try:
            Modulename = Modl.objects.get(name=PostData['ModuleName'])
            RunVersion = ModVersion.objects.get(name=PostData['VersionName'], module=Modulename)
            RunSuite1 = RunSuite(name=PostData['RunSuiteName'], mod_version=RunVersion, content=PostData['SuiteList'])
            RunSuite1.save()
            Result = json.dumps({'AddResult': 'OK'})
        except:
            Result = json.dumps({'AddResult': 'NO'})

    return HttpResponse(Result)


def CheckSuiteName(request):

    PostData = json.loads(request.body)
    if request.method == "POST":
        JobCheck = RunSuite.objects.filter(name=PostData['CheckSuiteName'])
        JobNumber = JobCheck.count()
        if (JobNumber == 0):
            CheckResult = json.dumps({'CheckResult': 'YES'})
        else:
            CheckResult = json.dumps({'CheckResult': 'NO'})
    return HttpResponse(CheckResult)


def ConfigUpdateVersion(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        VersionID = ModVersion.objects.filter(name=PostData['VersionName'], module=(Modl.objects.filter(name=PostData['ModuleName'])))
        SuiteName = TestSuite.objects.filter(mod_version=VersionID)
        RunSuiteName = RunSuite.objects.filter(mod_version=VersionID)
        RunSuiteNumber = RunSuiteName.count()
        SuiteNumber = SuiteName.count()
        SuiteList = []
        RunSuiteList=[]
        for i in range(0, SuiteNumber):
            SuiteList.append(SuiteName[i].name)
        for j in range(0, RunSuiteNumber):
            RunSuiteList.append(RunSuiteName[j].name)

    UpdateResult = json.dumps({'SuiteList': SuiteList, 'RunSuiteList':RunSuiteList})

    return HttpResponse(UpdateResult)

def ConfigUpdateSuite(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        RunSuiteName = RunSuite.objects.get(name=PostData['SuiteName'])

        SuiteName = RunSuiteName.content
        ListSuite = SuiteName.split('|')
        PostSuite=[]
        for index in ListSuite:
            if index != "":
                PostSuite.append(index)

    UpdateResult = json.dumps({'SuiteList': PostSuite})

    return HttpResponse(UpdateResult)


