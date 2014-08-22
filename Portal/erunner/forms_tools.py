#coding=utf-8
from django.forms import ModelForm
from models_dimension import Attachments


class UploadFileForm(ModelForm):
    class Meta:
        model = Attachments
        fields = ['name','description','instruction','file','created_time','is_active']