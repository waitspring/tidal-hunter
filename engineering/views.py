#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
engineering.views
"""


from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .forms import ProductionForm
from .models import Production, Project


# =====================================================================================================================
# production view set
# =====================================================================================================================
@login_required()
def production(request):
    if request.method == "GET":
        if request.GET.get("name") != None:
            pass
        elif request.GET.get("edit") != None:
            pass
        elif request.GET.get("add") != None:
            form = ProductionForm
            context = {
                "form": form
            }
            return render(request, "engineering/production_edit.html", context)
        elif request.GET.get("delete") != None:
            pass
        else:
            productions = Production.objects.all()
            context = {
                "productions": productions
            }
            return render(request, "engineering/productions_list.html", context)
    elif request.method == "POST":
        if request.GET.get("edit") != None:
            pass
        elif request.GET.get("add") != None:
            form = ProductionForm(request.POST)
            context = {
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # check field's value
                # =====================================================================================================
                try:
                    check_name = Production.objects.get(name=form.cleaned_data["name"])
                except:
                    check_name = None
                if check_name:
                    context["warn_name"] = "该产品线已经存在, 请勿重复添加"
                    return render(request, "engineering/production_edit.html", context)
                try:
                    check_tag = Production.objects.get(tag=form.cleaned_data["tag"])
                except:
                    check_tag = None
                if check_tag:
                    context["warn_tag"] = "该产品标识已经被使用, 请重新指定一个有效的产品标识"
                    return render(request, "engineering/production_edit.html", context)
                # =====================================================================================================
                form.save()
                return HttpResponseRedirect(reverse("production"))
            else:
                return render(request, "engineering/production_edit.html", context)
        else:
            return HttpResponseBadRequest(content="POST 错误 *** 错误定位到 engineering.views.production")
    else:
        return HttpResponseBadRequest(content="request 错误 *** 错误定位到 engineering.views.production")