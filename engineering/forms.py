#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
engineering.forms
"""


from django.forms import *
from .models import Production


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