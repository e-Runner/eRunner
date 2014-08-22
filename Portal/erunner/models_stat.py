from django.db import models
from django.utils import timezone
from models_fact import Jobs, ResultJob
from models_dimension import Modl, TestCase, ResultDesc, StatusDesc, FailureReason


class StatModule(models.Model):
    model = models.ForeignKey(Modl)
    manual_case_num = models.IntegerField()
    auto_case_num = models.IntegerField()
    updated_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "model_id: %s, manual_case_num: %s, auto_case_num: %s" % (
            self.model.name, self.manual_case_num, self.auto_case_num)


class StatJob(models.Model):
    job = models.ForeignKey(Jobs)
    last_result_desc = models.ForeignKey(ResultDesc)
    last_no = models.IntegerField()
    last_duration = models.IntegerField()
    health_rate = models.IntegerField()
    last_success_time = models.DateTimeField(default=timezone.now)
    last_failure_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "job_id: %s, last_result_desc_id: %s, last_no: %s" % (
            self.job.name, self.last_result_desc.name, self.last_no)


class StatJobExecution(models.Model):
    job = models.ForeignKey(Jobs)
    module = models.ForeignKey(Modl)
    result_desc = models.ForeignKey(ResultDesc)
    duration = models.IntegerField()
    execution_no = models.IntegerField()
    status_desc = models.ForeignKey(StatusDesc)
    totol_num = models.IntegerField()
    pass_num = models.IntegerField()
    created_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "job: %s, execution_no: %s, result_desc: %s, duration: %s" % (
            self.job.name, self.execution_no, self.result_desc.name, self.duration)


class StatCaeExecution(models.Model):
    test_case = models.ForeignKey(TestCase)
    module = models.ForeignKey(Modl)
    result_desc = models.ForeignKey(ResultDesc)
    result_job = models.ForeignKey(ResultJob)
    failure_reason = models.ForeignKey(FailureReason)
    duration = models.IntegerField()
    execution_no = models.IntegerField()
    created_time = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "job: %s, execution_no: %s, result_desc: %s, duration: %s" % (
            self.job.name, self.execution_no, self.result_desc.name, self.duration)