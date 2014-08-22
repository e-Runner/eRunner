__author__ = 'honglei.yu'
#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from erunner.models import Project
from erunner.models_dimension import Modl
from erunner.models_dimension import ModVersion
from erunner.models_dimension import TestSuite
from erunner.models_dimension import RunSuite
from erunner.models_fact import Jobs
from erunner.models_fact import ResultJob
import json

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def report(request):
    return render_to_response('report.html', context_instance=RequestContext(request))

def ReportProductChanged(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        ModuleName = Project.objects.filter(ProductName=PostData['ProductName'])
        ModuleNumber = ModuleName.count()
        ModuleNameSort = []
        for i in range(0, ModuleNumber):
            ModuleNameSort.append(ModuleName[i].ProjectName)
        ResultReport = json.dumps({'ModuleSortName' : ModuleNameSort})
        return HttpResponse(ResultReport)

def ReportModuleChanged(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        ModuleName = Modl.objects.get(name=PostData['ModuleName'])
        ModuleVersion = ModVersion.objects.filter(module=ModuleName)
        JobList = []
        for i in range(ModuleVersion.count()):
            Suite = RunSuite.objects.filter(mod_version=ModuleVersion[i])
            for j in range(Suite.count()):
                JobName=Jobs.objects.filter(test_suite=Suite[j], is_active=1)
                for k in range(JobName.count()):
                    JobList.append(JobName[k].name)
        ReportResult = json.dumps({'JobSortName' : JobList})
        return HttpResponse(ReportResult)

def ReportJobChanged(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        JobName = Jobs.objects.get(name=PostData['JobName'])
        JobTestResult = ResultJob.objects.filter(job=JobName).order_by('-start_time')
        Joblist = []
        for item in JobTestResult:
            try:
                IndexResult={}
                IndexResult['JobId'] = item.id
                IndexResult['JobName']=PostData['JobName']
                TotalNumber = item.pass_num+item.fail_num
                IndexResult['TotalNumber']=TotalNumber
                IndexResult['PassNumber'] = item.pass_num
                ratio = "%.4f"%(float(item.pass_num)/TotalNumber)
                IndexResult['Ratio'] = "%.2f"%(100*(float(ratio)))
                IndexResult['StartTime'] = str(item.start_time)
                IndexResult['DurationTime'] = (item.end_time-item.start_time).seconds
                Joblist.append(IndexResult)
            except:
                pass
        JobReport = json.dumps({'JobResult':Joblist})
        return HttpResponse(JobReport)