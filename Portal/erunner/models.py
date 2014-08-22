from django.db import models
from models_dimension import *
from models_fact import *
from models_stat import *


class Id(models.Model):
    Module = models.CharField(max_length=30)
    IP = models.CharField(max_length=20)
    Port = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.Module

class Cascade(models.Model):
    ProductName = models.CharField(max_length=30)
    ProjectName = models.CharField(max_length=30)
    SubProject = models.CharField(max_length=30)
    TestVersion = models.CharField(max_length=30)
    TestLevel = models.CharField(max_length=30)


class Product(models.Model):
    JobName = models.CharField(max_length=30)
    ProductName = models.CharField(max_length=30)
    ProjectName = models.CharField(max_length=30)
    ModuleName = models.CharField(max_length=30)
    TestVersion = models.CharField(max_length=30)
    TestLevel = models.CharField(max_length=30)
    TestTime = models.CharField(max_length=30)
    TestStatus = models.CharField(max_length=30)


class Project(models.Model):
    ProductName = models.CharField(max_length=30)
    ProjectName = models.CharField(max_length=30)

class Module(models.Model):
    ProjectName = models.CharField(max_length=30)
    ModuleName = models.CharField(max_length=30)

class Version(models.Model):
    ProductName = models.CharField(max_length=30)
    TestVersion = models.CharField(max_length=30)

class Level(models.Model):
    ProjectName = models.CharField(max_length=30)
    TestLevel = models.CharField(max_length=30)

class Result(models.Model):
    Module = models.CharField(max_length=30)
    Version = models.CharField(max_length=20)
    CaseNum = models.CharField(max_length=20)
    Result = models.CharField(max_length=20)
    ExecDataTime = models.DateTimeField(null=True, blank=True)
    ExecIndex = models.NullBooleanField(null=True, blank=True)

    def __unicode__(self):
        return self.Version

class JobScheduler(models.Model):
    JobNumber = models.IntegerField()
    JobName = models.CharField(max_length=30)
    JobTime = models.CharField(max_length=30)

class Job(models.Model):
    JobHealth = models.CharField(max_length=30)
    JobName = models.CharField(max_length=30)
    LastResult = models.CharField(max_length=30)
    StartTime = models.CharField(max_length=30)
    JobStatus = models.CharField(max_length=30)
    ProductName = models.CharField(max_length=30)

class JobResult(models.Model):
    JobName = models.CharField(max_length=30)
    JobResult = models.CharField(max_length=20)
    TotalNumber = models.IntegerField()
    PassedNumber = models.IntegerField()
    StartTime = models.DateTimeField(null=True, blank=True)
    DurationTime = models.IntegerField()

class Statistics(models.Model):
    Module = models.CharField(max_length=30)
    Version = models.CharField(max_length=30)
    ExecStartTime = models.DateTimeField(null=True, blank=True)
    ExecEndTime = models.DateTimeField(null=True, blank=True)
    TotalNum = models.IntegerField(null=True, blank=True)
    Environment = models.CharField(max_length=30)

    def __unicode__(self):
        return self.Version