#!/usr/bin/python3
# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import login, logout


# ===========================================================================================================
# config account urls
# ===========================================================================================================
urlpatterns = [
    url(r"^login/$", login, name="login"),
    url(r"^logout/$", logout, name="logout")
]