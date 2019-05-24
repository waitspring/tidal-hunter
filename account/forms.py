#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
account.forms
"""


import re
from django.forms import *
from django.contrib import auth
from .models import Employee, Department
from engineering.models import Production, Project


# =====================================================================================================================
# login / logout form part
# =====================================================================================================================
class LoginForm(Form):
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


# =====================================================================================================================
# users (employees too) controlling form part
# =====================================================================================================================
class EmployeeAddForm(ModelForm):
    """
    this form reuse the model Employee, and we use this form class to add user account, we have used some
    clean_<fields> functions, and the clean( ) function would be called by EmployeeAddForm.is_valid( ) too
    """
    class Meta:
        model = Employee
        exclude = (
            "id", "is_superuser", "is_staff", "timestamps", "last_login"
        )
        widgets = {
            "username": TextInput(
                attrs={"class": "form-control my-input", "placeholder": "cannot be updated after submission"}
            ),
            "password": PasswordInput(
                attrs={"class": "form-control my-input", "placeholder": "Password with more than 6 digits"}
            ),
            "nickname": TextInput(
                attrs={"class": "form-control my-input", "placeholder": "cannot be updated after submission"}
            ),
            "email": EmailInput(attrs={"class": "form-control my-input"}),
            "phone": TextInput(attrs={"class": "form-control my-input"}),
            "sequence": Select(attrs={"class": "form-control my-input"}),
            "grade": Select(attrs={"class": "form-control my-input"}),
            "education": Select(attrs={"class": "form-control my-input"}),
            "department": Select(attrs={"class": "form-control my-input"}),
            "is_active": Select(choices=((True, "正常"), (False, "冻结")), attrs={"class": "form-control my-input"}),
            "add_date": DateInput(attrs={"class": "form-control my-input"})
        }

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise ValidationError("请输入 6 位以上的有效密码")
        return password

    def clean_username(self):
        """
        because of the fields define order in account.models.Employee model , we only cloud get username field value in
        this check function by self.cleaned_date
        """
        username = self.cleaned_data.get("username")
        try:
            check = Employee.objects.get(username=username)
        except:
            check = None
        if check:
            raise ValidationError("该用户名称已经被占用")
        return username

    def clean_nickname(self):
        """
        like the clean_username( ), this function can get both username and nickname fields by self.cleaned_data
        """
        nickname = self.cleaned_data.get("nickname")
        try:
            check = Employee.objects.get(username=nickname)
        except:
            check = None
        if check:
            raise ValidationError("该同事已经具有一个账号, 请勿重复建立")
        return nickname

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if len(phone) != 11:
                raise ValidationError("手机号码格式错误")
            else:
                try:
                    int(phone)
                except ValueError:
                    raise ValidationError("手机号码格式错误")
                if not re.match(r"^1[3456789].*", phone):
                    raise ValidationError("手机号码格式错误")
        return phone


class EmployeeEditForm(ModelForm):
    """
    we use this form class to edit user account that had been created
    """
    class Meta:
        model = Employee
        exclude = (
            "id", "password", "is_superuser", "is_staff", "timestamps", "last_login"
        )
        widgets = {
            "username": TextInput(attrs={"class": "form-control my-input", "readonly": "readonly"}),
            "nickname": TextInput(attrs={"class": "form-control my-input", "readonly": "readonly"}),
            "email": EmailInput(attrs={"class": "form-control my-input"}),
            "phone": TextInput(attrs={"class": "form-control my-input"}),
            "sequence": Select(attrs={"class": "form-control my-input"}),
            "grade": Select(attrs={"class": "form-control my-input"}),
            "education": Select(attrs={"class": "form-control my-input"}),
            "department": Select(attrs={"class": "form-control my-input"}),
            "is_active": Select(choices=((True, "正常"), (False, "冻结")), attrs={"class": "form-control my-input"}),
            "add_date": DateInput(attrs={"class": "form-control my-input"})
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if len(phone) != 11:
                raise ValidationError("手机号码格式错误")
            else:
                try:
                    int(phone)
                except ValueError:
                    raise ValidationError("手机号码格式错误")
                if not re.match(r"^1[3456789].*", phone):
                    raise ValidationError("手机号码格式错误")
        return phone

    def clean_sequence(self):
        """
        we need to notice that if some projects or some productions has been owned by him, he is can not be changed his
        sequence information
        """
        sequence = self.cleaned_data["sequence"]
        try:
            productions = Production.objects.filter(manager=Employee.objects.get(username=self.cleaned_data["username"]))
        except:
            productions = None
        if productions and sequence != Employee.objects.get(username=self.cleaned_data["username"]).sequence:
            raise ValidationError("当前同事正在负责具体的产品或项目, 无法更新其工作序列")
        return self.cleaned_data["sequence"]


class PasswordControlForm(Form):
    """
    this form is used to reset the password of the specified user directly

    please attention that, this form is only used by super administrator
    """
    new_password = CharField(
        label="新密码",
        error_messages={"required": "请输入 6 位以上的有效密码"},
        widget=PasswordInput(attrs={"class": "form-control", "style": "width: 350px"})
    )
    new_password_again = CharField(
        label="确认新密码",
        error_messages={"required": "请再次输入 6 位以上的有效密码"},
        widget=PasswordInput(attrs={"class": "form-control", "style": "width: 350px"})
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordControlForm, self).__init__(*args, **kwargs)

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if len(new_password) < 6:
            raise ValidationError("请输入 6 位以上的有效密码")
        return new_password

    def clean_new_password_again(self):
        new_password = self.cleaned_data.get("new_password")
        new_password_again = self.cleaned_data.get("new_password_again")
        if new_password and new_password != new_password_again:
            raise ValidationError("两次密码的输入不一致")
        return new_password_again

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password_again"])
        if commit:
            self.user.save()
        return self.user


class PasswordEditForm(Form):
    """
    password edit form will be used by all users, enabling them to modify their passwords by themselves
    """
    old_password = CharField(
        label="旧密码",
        widget=PasswordInput(attrs={"class": "form-control", "style": "width: 350px"})
    )
    new_password = CharField(
        label="新密码",
        widget=PasswordInput(attrs={"class": "form-control", "style": "width: 350px"})
    )
    new_password_again = CharField(
        label="确认新密码",
        widget=PasswordInput(attrs={"class": "form-control", "style": "width: 350px"})
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordEditForm, self).__init__(*args, **kwargs)

    def clean_old_password(self):
        """
        attention again: because we would use the check function -- form.is_valid( ) in our views page, to check if the
        form value which had been submit by users is ok, this check function would call every clean_<field_name>
        function to check field's value one by one

        and:

            * if we define a field name old_password
            * then the check function need to be named clean_old_password( )
            * if we define a field name new_password
            * then the check function need to be named clean_new_password( )

        otherwise, we could name the check function clean( )
        """
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("原有密码输入错误")
        return old_password

    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if len(new_password) < 6:
            raise ValidationError("请输入 6 位以上的有效密码")
        return new_password

    def clean_new_password_again(self):
        new_password = self.cleaned_data.get("new_password")
        new_password_again = self.cleaned_data.get("new_password_again")
        if new_password and new_password != new_password_again:
            raise ValidationError("两次密码的输入不一致")
        return new_password_again

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password_again"])
        if commit:
            self.user.save()
        return self.user


# =====================================================================================================================
# department edit form, include adding and editing two parts
# =====================================================================================================================
class DepartmentForm(ModelForm):
    """
    a form class that combines new data or existing data for a department
    """
    class Meta:
        model = Department
        exclude = (
            "id", "timestamps"
        )
        widgets = {
            "self_name": TextInput(attrs={"class": "form-control my-input"}),
            "full_name": TextInput(attrs={"class": "form-control my-input"}),
            "father": Select(attrs={"class": "form-control my-input"}),
            "header": Select(attrs={"class": "form-control my-input"}),
            "add_date": DateInput(attrs={"class": "form-control my-input"})
        }

    def clean(self):
        """
        we need to check the foreign key father so that we could update our full_name field value, and we can save this
        field value after noon
        """
        father = self.cleaned_data.get("father")
        if father:
            self.cleaned_data["full_name"] = father.full_name + " / " + self.cleaned_data["self_name"]
        else:
            self.cleaned_data["full_name"] = self.cleaned_data["self_name"]