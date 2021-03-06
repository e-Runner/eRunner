import re
from django.core import validators
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Prod(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid product name.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class SubFW(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid sub-framework name.', 'invalid')
        ])
    protocol = models.CharField(max_length=10, blank=True)
    ip = models.CharField(max_length=20)
    port = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Modl(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-_]+$'), 'Enter a valid module name.', 'invalid')
        ])
    product = models.ForeignKey(Prod)
    sub_fw = models.ForeignKey(SubFW)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class SubModl(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid sub-module name.', 'invalid')
        ])
    module = models.ForeignKey(Modl)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Importance(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid importance name.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class TestLevel(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test level name.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class ModVersion(models.Model):
    name = models.CharField(max_length=60,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid module version name.', 'invalid')
        ])
    module = models.ForeignKey(Modl)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name', 'module')

    def __unicode__(self):
        return self.name


class TestCase(models.Model):
    name = models.CharField(max_length=60, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-_]+$'), 'Enter a valid test case name.', 'invalid')
        ])
    version = models.IntegerField(blank=True)
    sub_module = models.ForeignKey(SubModl)
    importance = models.ForeignKey(Importance)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class TestSuite(models.Model):
    name = models.CharField(max_length=60,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test case name.', 'invalid')
        ])
    mod_version = models.ForeignKey(ModVersion)
    test_level = models.ForeignKey(TestLevel)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class RunSuite(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test case name.', 'invalid')
        ])
    mod_version = models.ForeignKey(ModVersion)
    content = models.CharField(max_length=2014)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class FailureReason(models.Model):
    name = models.CharField(max_length=50, unique=True,
        help_text='Required. 50 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test case name.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class StatusDesc(models.Model):
    name = models.CharField(max_length=80, unique=True,
        help_text='Required. 80 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test case name.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class ResultDesc(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test result description.', 'invalid')
        ])
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Attachments(models.Model):
    name = models.CharField(max_length=30, unique=True,
        help_text='Required. 30 characters or fewer',
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'Enter a valid test result description.', 'invalid')
        ])
    description = models.CharField(max_length=200, blank=True)
    instruction = models.CharField(max_length=500, blank=True)
    file=models.FileField(upload_to="../upload/")
    created_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.namei