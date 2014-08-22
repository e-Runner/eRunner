__author__ = 'honglei.yu'
# the function of this file is to process the core data and schedule
from django.http import HttpResponse
from erunner.models_dimension import TestSuite
from erunner.models_dimension import Prod
from erunner.models_dimension import RunSuite
from erunner.models_dimension import ModVersion
from erunner.models_dimension import Modl
from erunner.models_dimension import SubFW
from erunner.models_dimension import ResultDesc
from erunner.models_dimension import TestLevel
from erunner.models_fact import ResultJob
from erunner.models_stat import StatJob
from erunner.models_dimension import SubModl
from erunner.models_dimension import Importance
from erunner.models_dimension import TestCase
from erunner.models_fact import ResultCase


from django.contrib.auth.models import User
from erunner.models_fact import Jobs
from django.utils import timezone
from datetime import datetime

import socket
import json

def RunJob(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        JobRun = Jobs.objects.get(name=PostData['JobName'])
        SuiteRun = RunSuite.objects.get(id=JobRun.test_suite_id)
        SuiteList = SuiteRun.content
        ListSuite = SuiteList.split('|')
        PostSuite=[]
        for index in ListSuite:
            if index != "":
                PostSuite.append(index)
        VersionRun = ModVersion.objects.get(id=SuiteRun.mod_version_id)
        ModuleRun = Modl.objects.get(id=VersionRun.module_id)
        ProductRun = Prod.objects.get(id=ModuleRun.product_id)
        FrameRun = SubFW.objects.get(id=ModuleRun.sub_fw_id)

        SocketData = {
            "JobName": JobRun.name,
            "ProductName":ProductRun.name,
            "TestModule": ModuleRun.name,
            "TestVersion": VersionRun.name,
            "TestSuite": SuiteRun.name,
            "TestSuiteList":PostSuite,
            "Executor":'honglei.yu'
        }
        print(SocketData)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((FrameRun.ip, int(FrameRun.port)))
        except:
            RunResult = json.dumps({'RunResult': 'NO'})
        else:
            sock.send(json.dumps(SocketData))
            RecvMessage = sock.recv(1024)
            RunResult = json.dumps({'RunResult': RecvMessage, 'RunJobName': PostData['JobName']})

    return HttpResponse(RunResult)


def PostTestResult(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        pass_number = 0
        fail_number = 0
        block_number = 0
        omit_number = 0
        for k in range(0, len(PostData['returnvalue'])):
            if (PostData['returnvalue'][k]['TestResult']).upper() == "PASSED":
                pass_number = pass_number+1
            elif (PostData['returnvalue'][k]['TestResult']).upper() == "FAILED":
                fail_number = fail_number+1
            elif (PostData['returnvalue'][k]['TestResult']).upper() == "BLOCKED":
                block_number = block_number+1
            else:
                omit_number = omit_number+1
        if (fail_number != 0)or(block_number!=0)or(omit_number!=0):
            test_job_result = "Failed"
        else:
            test_job_result = "Passed"
        result_job = Jobs.objects.get(name=PostData['JobName'])
        result_descr = ResultDesc.objects.get(name=test_job_result)
        user_case = User.objects.get(username=PostData['UserName'])

        job_result = ResultJob(job=result_job, result_desc=result_descr,start_time=PostData['StartTime'], end_time=PostData['EndTime'], executor=user_case,
                               pass_num=pass_number, fail_num=fail_number, block_num=block_number,
                               omit_num = omit_number)
        job_result.save()
        for_stat_job = ResultJob.objects.filter(job=result_job)
        resultall=for_stat_job.count()
        passindex=0
        for item in for_stat_job:
            if (str(item.result_desc)).upper() == "PASSED":
                passindex=passindex+1
        resultratio = int(passindex*100/resultall)
        stat_job = StatJob.objects.get(job=result_job)
        stat_job.last_no=stat_job.last_no+1
        stat_job.last_result_desc=result_descr
        if test_job_result.upper() == "PASSED":
            stat_job.last_success_time=timezone.now()
        else:
            stat_job.last_failure_time=timezone.now()
        stat_job.health_rate=resultratio
        stat_job.last_duration=PostData['DurationTime']
        stat_job.save()

        sub_module = SubModl.objects.get(name=PostData['submodule'])
        case_importance = Importance.objects.get(name='Average')
        for i in range(0, len(PostData['returnvalue'])):
            try:
                testcase = TestCase(name=PostData['returnvalue'][i]['TestCase'], version=1, sub_module=sub_module, importance=case_importance)
                testcase.save()
            except:
                pass
        for j in range(0,  len(PostData['returnvalue'])):
            try:
                case_test = TestCase.objects.get(name=PostData['returnvalue'][j]['TestCase'])
                case_descr = ResultDesc.objects.get(name=PostData['returnvalue'][j]['TestResult'])
                posttime =datetime.strptime(PostData['StartTime'], '%Y-%m-%d %H:%M:%S.%f')
                posttime = posttime.strftime("%Y%m%d%H%M%S")
                url = PostData['ProductName']+'|'+PostData['submodule']+'|'+PostData['JobName']+'-'+posttime+'|'+PostData['returnvalue'][j]['TestCase']
                case_result = ResultCase(test_case=case_test, result_job=job_result, start_time=PostData['StartTime'], result_desc=case_descr,log_url=url,bug_id='')
                case_result.save()
            except:
                pass
    PostResult = json.dumps({'Result':'OK'})
    return HttpResponse(PostResult)

def FileChangedHandled(request):
    PostData = json.loads(request.body)
    if request.method == "POST":
        Test_Version = PostData['Version']
        Module_Name = PostData['ModuleName']
        Test_Suite = PostData['TestSuite']
        TestVersion = ModVersion.objects.filter(name=Test_Version)
        Test_Level = TestLevel.objects.get(name='Average')
        if TestVersion.count() == 0:
            ModuleName = Modl.objects.get(name=Module_Name)
            VersionTest = ModVersion(name=Test_Version, module=ModuleName)
            VersionTest.save()
            NewVersion = ModVersion.objects.get(name=Test_Version)
            for SuiteName in Test_Suite:
                Suite_Name = TestSuite(name=SuiteName, mod_version=NewVersion, test_level=Test_Level)
                Suite_Name.save()
        else:
            Suite_List = TestSuite.objects.filter(mod_version=TestVersion[0])
            Suite_List.delete()
            InsertVersion = ModVersion.objects.get(name=Test_Version)
            for SuiteName in Test_Suite:
                Suite_Name = TestSuite(name=SuiteName, mod_version=InsertVersion, test_level=Test_Level)
                Suite_Name.save()

    return HttpResponse(json.dumps({'Result':'OK'}))
