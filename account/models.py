#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
account.models

we will define some models for tidal hunter in this models.py
"""


from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as lazy
from django.utils import timezone
from django.db import models
from django.db.models import *


# =====================================================================================================================
# tidal hunter user's model is Employee class
# =====================================================================================================================
class EmployeeManager(BaseUserManager):
    """
    EmployeeManager class is the ancillary management tool for Employee class
    """
    def create_employee(self, username, nickname, password=None):
        employee = self.model(username=username, nickname=nickname)
        employee.set_password(password)
        employee.save(using=self._db)
        return employee

    def create_superuser(self, username, nickname, password):
        superuser = self.create_employee(username=username, nickname=nickname, password=password)
        superuser.is_active = True
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser


class Employee(AbstractBaseUser):
    """
    we will define a new user model named Employee as tidal hunter's accounts style

    *******************************************************************************************************************

    please check the tidal.settings file and make sure we have made the AUTH_USER_MODEL = "account.Employee", otherwise
    system will use django.contrib.auth.models.User as tidal hunter's accounts style
    """
    sequence_choices = (
        ("产品设计师", "产品设计师"),
        ("交互设计师", "交互设计师"),
        ("项目管理师", "项目管理师"),
        ("开发工程师", "开发工程师"),
        ("数据工程师", "数据工程师"),
        ("测试工程师", "测试工程师"),
        ("运维工程师", "运维工程师"),
        ("市场和运营", "市场和运营")
    )

    grade_choices = (
        ("P2 助理职级", "P2 助理职级"),
        ("P3 助理职级", "P3 助理职级"),
        ("P4 专业职级", "P4 专业职级"),
        ("P5 专业职级", "P5 专业职级"),
        ("P6 专家职级", "P6 专家职级"),
        ("P7 专家职级", "P7 专家职级"),
        ("P8 管理职级", "P8 管理职级"),
        ("P9 管理职级", "P9 管理职级")
    )

    eduction_choices = (
        ("专科", "专科"),
        ("本科", "本科"),
        ("硕士研究生", "硕士研究生"),
        ("博士研究生", "博士研究生")
    )

    username = CharField(lazy("用户名称"), max_length=30, unique=True, blank=False, null=False)
    nickname = CharField(lazy("中文名字"), max_length=30, unique=True, blank=False, null=False)
    email = EmailField(lazy("电子邮箱"), max_length=255, blank=True, null=True)
    phone = CharField(lazy("联系电话"), max_length=11, blank=True, null=True)
    sequence = CharField(lazy("工作岗位"), choices=sequence_choices, max_length=30, blank=True, null=True)
    grade = CharField(lazy("工作职级"), choices=grade_choices, max_length=30, blank=True, null=True)
    education = CharField(lazy("学历背景"), choices=eduction_choices, max_length=30, blank=True, null=True)

    department = ForeignKey(
        "Department", related_name="employee_department", verbose_name=lazy("所属部门"),
        max_length=255, blank=True, null=True, on_delete=SET_NULL
    )

    is_superuser = BooleanField(lazy("超级权限"), default=False)
    is_staff = BooleanField(lazy("后台权限"), default=False)
    is_active = BooleanField(lazy("用户状态"), default=True)
    add_date = DateField(lazy("入职日期"), default=timezone.now, blank=True, null=True)
    timestamps = DateTimeField(lazy("时间戳"), default=timezone.now)
    objects = EmployeeManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "nickname", "email"
    ]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nickname

    def __str__(self):
        return self.nickname


# =====================================================================================================================
# department or group class part
# =====================================================================================================================
class Department(models.Model):
    """
    django do not support define ourselves' group class
    """
    self_name = CharField(lazy("部门名称"), max_length=30, blank=False, null=False)
    full_name = CharField(lazy("部门全称"), max_length=255, unique=True, blank=True, null=True)

    father = ForeignKey(
        "self", verbose_name=lazy("上级部门"),
        max_length=255, blank=True, null=True, on_delete=SET_NULL
    )
    header = ForeignKey(
        Employee, related_name="department_header", verbose_name=lazy("部门领导"),
        limit_choices_to={"is_staff": False},
        max_length=30, blank=True, null=True, on_delete=SET_NULL
    )

    add_date = DateField(lazy("成立日期"), default=timezone.now, blank=True, null=True)
    timestamps = DateTimeField(lazy("时间戳"), default=timezone.now)

    def __str__(self):
        return self.full_name