# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import login, logout, employee, department, myself


# =====================================================================================================================
# config account urls
# =====================================================================================================================
urlpatterns = [
    url(r"^login/$", login, name="login"),
    url(r"^logout/$", logout, name="logout"),
    url(r"^employees/$", employee, name="employee"),
    url(r"^departments/$", department, name="department"),
    url(r"^myself/$", myself, name="myself")
]