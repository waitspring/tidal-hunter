#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
engineering.models

define all engineering models in this file
"""


from django.utils.translation import ugettext_lazy as lazy
from django.utils import timezone
from django.db.models import *
from account.models import Employee, Department


# =====================================================================================================================
# define data models related to production lines
# =====================================================================================================================
class Production(Model):
    """
    the production line data model
    """
    user_choices = (
        ("内部员工", "内部员工"),
        ("合作伙伴", "合作伙伴"),
        ("企业用户", "企业用户"),
        ("个人用户", "个人用户")
    )

    name = CharField(lazy("产品名称"), max_length=30, db_index=True)
    tag = CharField(lazy("产品标识"), max_length=30, db_index=True)
    description = TextField(lazy("产品描述"), max_length=255, blank=True, null=True)
    user = CharField(lazy("产品用户"), choices=user_choices, max_length=30, blank=True, null=True)

    manager = ForeignKey(
        Employee, verbose_name=lazy("产品经理"),
        max_length=30, blank=True, null=True, on_delete=SET_NULL
    )
    department = ForeignKey(
        Department, verbose_name=lazy("运营部门"),
        max_length=255, blank=True, null=True, on_delete=SET_NULL
    )

    add_date = DateField(lazy("添加日期"), default=timezone.now, blank=True, null=True)
    timestamps = DateTimeField(lazy("时间戳"), default=timezone.now)

    def __str__(self):
        return self.name


# =====================================================================================================================
# define data models related to project lines
# =====================================================================================================================
class Project(Model):
    """
    the project line data model
    """
    language_choices = (
        ("c/c++", "c/c++"),
        ("c#", "c#"),
        ("go", "go"),
        ("html5", "html5"),
        ("java", "java"),
        ("javascript", "javascript"),
        ("php", "php"),
        ("python/python3", "python/python3"),
        ("ruby", "ruby"),
        ("shell", "shell"),
        ("others", "others")
    )
    arch_choices = (
        ("django", "django"),
        ("dubbo", "dubbo"),
        ("flask", "flask"),
        ("reactjs", "reactjs"),
        ("nodejs", "nodejs"),
        ("spring boot", "spring boot"),
        ("spring cloud", "spring cloud"),
        ("scala", "scala"),
        ("scrapy", "scrapy"),
        ("vuejs", "vuejs")
    )
    genre_choices = (
        ("frontend", "frontend program"),
        ("middleware", "middleware program"),
        ("backend", "backend program")
    )
    status_choices = (
        ("online", "迭代正常"),
        ("stay for online", "等待上线"),
        ("stay for offline", "等待下线"),
        ("offline", "已经下线")
    )

    self_name = CharField(lazy("工程私有名称"), max_length=30, blank=False, null=False)
    full_name = CharField(lazy("工程名称"), max_length=255, unique=True, blank=True, null=True)
    self_tag = CharField(lazy("工程私有标识"), max_length=30, blank=False, null=False)
    full_tag = CharField(lazy("工程标识"), max_length=255, unique=True, blank=True, null=True)
    domain = CharField(lazy("域名配置"), max_length=255, blank=True, null=True)
    git_source = CharField(lazy("代码托管地址"), max_length=255, blank=True, null=True)
    description = TextField(lazy("工程描述"), max_length=255, blank=True, null=True)
    language = CharField(lazy("工程语言"), choices=language_choices, max_length=30, blank=True, null=True)
    arch = CharField(lazy("工程架构"), choices=arch_choices, max_length=30, blank=True, null=True)
    genre = CharField(lazy("工程类型"), choices=genre_choices, max_length=30, blank=True, null=True)
    status = CharField(lazy("工程状态"), choices=status_choices, max_length=30, blank=True, null=True)

    production = ForeignKey(
        Production, verbose_name=lazy("所属产品"),
        max_length=30, blank=False, null=False
    )
    developer = ForeignKey(
        Employee, related_name=lazy("developer"), verbose_name=lazy("开发负责人"),
        max_length=30, blank=True, null=True, on_delete=SET_NULL
    )
    tester = ForeignKey(
        Employee, related_name=lazy("tester"), verbose_name=lazy("测试负责人"),
        max_length=30, blank=True, null=True, on_delete=SET_NULL
    )
    operator = ForeignKey(
        Employee, related_name=lazy("operator"), verbose_name=lazy("运维负责人"),
        max_length=30, blank=True, null=True, on_delete=SET_NULL
    )

    add_date = DateField(lazy("添加时间"), default=timezone.now, blank=True, null=True)
    timestamps = DateTimeField(lazy("时间戳"), default=timezone.now)

    def __str__(self):
        return self.full_name