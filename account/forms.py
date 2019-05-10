#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
account.forms
"""


from django.forms import *
from django.contrib import auth
from .models import Employee, Department


# =====================================================================================================================
# login / logout form part
# =====================================================================================================================
class LoginForm(forms.Form):
    """
    connect the account.views.login, we need to construct two fields (username and password) in this form
    """
    username = CharField(
        label="Username",
        error_messages={"required": "必须填写有效的用户名称"},
        widget=TextInput(attrs={"class": "form-control"})
    )
    password = CharField(
        label="Password",
        error_messages={"required": "必须填写有效的登录密码"},
        widget=PasswordInput(attrs={"class": "form-control"})
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.auth_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        """
        use the clean_<field_name> function to check field_name value, in this function, we will check the username and
        the password too

        attention: we take auth.authenticate( ) for checking if inputting username and password is right, and if
        checking result is True, the auth.authenticate( ) will return a user class, or return None
        """
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            self.auth_cache = auth.authenticate(username=username, password=password)
            if not self.auth_cache:
                raise ValidationError("账号和密码不匹配, 或账户过期")
        return self.cleaned_data

    def get_auth_cache(self):
        """
        this function will return user's account information as cache data for verifying the execution permissions for
        every function
        """
        return self.auth_cache