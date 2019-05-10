#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
tidal.urls

urls.py is the root url configure file with tidal hunter project, this file will receive all requests and distribute
them into our applications
"""


from django.conf.urls import include, url
from board.views import board


# =====================================================================================================================
# path config
# =====================================================================================================================
urlpatterns = [
    url(r"^accounts/", include("account.urls")),
    url(r"^$", board, name="board")
]