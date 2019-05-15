#!/usr/bin/python3
# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import production


# =====================================================================================================================
# config engineering urls
# =====================================================================================================================
urlpatterns = [
    url(r"^productions/$", production, name="production")
]