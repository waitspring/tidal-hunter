#!/usr/bin/python3
# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import production, project, deploy


# =====================================================================================================================
# config engineering urls
# =====================================================================================================================
urlpatterns = [
    url(r"^productions/$", production, name="production"),
    url(r"^projects/$", project, name="project"),
    url(r"^cicd/$", deploy, name="deploy")
]