#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
engineering.forms
"""


from django.forms import *
from .models import Production, Project


# =====================================================================================================================
# production form configuration
# =====================================================================================================================
class ProductionForm(ModelForm):
    """
    production form
    """
    class Meta:
        model = Production
        exclude = (
            "id", "timestamps"
        )
        widgets = {
            "name": TextInput(attrs={"class": "form-control my-input"}),
            "tag": TextInput(attrs={"class": "form-control my-input"}),
            "description": Textarea(attrs={"class": "form-control my-input"}),
            "user": Select(attrs={"class": "form-control my-input"}),
            "manager": Select(attrs={"class": "form-control my-input"}),
            "department": Select(attrs={"class": "form-control my-input"}),
            "add_date": DateInput(attrs={"class": "form-control my-input"})
        }


# =====================================================================================================================
# project form configuration
# =====================================================================================================================
class ProjectForm(ModelForm):
    """
    project form
    """
    class Meta:
        model = Project
        exclude = (
            "id", "timestamps"
        )
        widgets = {
            "self_name": TextInput(attrs={"class": "form-control my-input"}),
            "full_name": TextInput(attrs={"class": "form-control my-input"}),
            "self_tag": TextInput(attrs={"class": "form-control my-input"}),
            "full_tag": TextInput(attrs={"class": "form-control my-input"}),
            "domain": TextInput(attrs={"class": "form-control my-input"}),
            "git_source": TextInput(attrs={"class": "form-control my-input"}),
            "description": Textarea(attrs={"class": "form-control my-input"}),
            "language": Select(attrs={"class": "form-control my-input"}),
            "arch": Select(attrs={"class": "form-control my-input"}),
            "genre": Select(attrs={"class": "form-control my-input"}),
            "status": Select(attrs={"class": "form-control my-input"}),
            "production": Select(attrs={"class": "form-control my-input"}),
            "developer": Select(attrs={"class": "form-control my-input"}),
            "tester": Select(attrs={"class": "form-control my-input"}),
            "operator": Select(attrs={"class": "form-control my-input"}),
            "add_date": DateInput(attrs={"class": "form-control my-input"})
        }

    def clean_add_date(self):
        """
        we know that if a project has been owned by a production, its add_date must be after by production's add_date,
        and in this function, we will check it
        """
        project_add_date = self.cleaned_data.get("add_date")
        production_add_date = self.cleaned_data.get("production").add_date
        if project_add_date < production_add_date:
            raise ValidationError("日期输入错误, 工程开始日期不可能早于产品开始日期")
        else:
            return project_add_date

    def clean(self):
        """
        we need to deal the full_name and full_tag fields in the last clean function
        """
        production = self.cleaned_data.get("production")
        self.cleaned_data["full_name"] = production.name + '-' + self.cleaned_data.get("self_name")
        self.cleaned_data["full_tag"] = production.tag + '-' + self.cleaned_data.get("self_tag")
#        try:
#            check = Project.objects.get(full_name=full_name)
#        except:
#            check = None
#        if check:
#            raise ValidationError("产品内已经配置该工程, 请勿重复添加")
#        try:
#            check = Project.objects.get(full_tag=full_tag)
#        except:
#            check = None
#        if check:
#            raise ValidationError("当前工程标识已经被占用, 请重新输入一个有效的工程标识")