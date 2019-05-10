#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
account.views
"""


from django.shortcuts import HttpResponseRedirect, render, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from .models import Employee, Department


# ===========================================================================================================
# login / logout view part
# ===========================================================================================================
def login(request):
    """
    we use the function django.contrib.auth.decorators.login_required as a decorator, if user have not login
    tidal hunter, we need to redirect his page into login page, like this:

        * /accounts/login/?next=/

    and the parameter next will value the user's original access route
    """
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == "GET" and request.GET.get("next"):
        next_page = request.GET.get("next")
    else:
        next_page = '/'
    if next_page == "/accounts/logout/":
        next_page = '/'
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_auth_cache())
            return HttpResponseRedirect(request.POST.get("next"))
    else:
        form = LoginForm(request)
    context = {
        "form": form,
        "next": next_page
    }
    return render(request, "account/login.html", context)


@login_required()
def logout(request):
    """
    we could use the dict request.META which include this http request's header information, like as:

        * ip address
        * browser's type and status

    request.META["HTTP_REFERER"] is the link address that where is user login tidal hunter from
    """
    auth.logout(request)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])