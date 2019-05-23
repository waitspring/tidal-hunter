#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
engineering.views
"""


from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from .forms import ProductionForm, ProjectForm
from .models import Production, Project


# =====================================================================================================================
# production view set
# =====================================================================================================================
@login_required()
def production(request):
    if request.method == "GET":
        if request.GET.get("name") != None:
            production = Production.objects.get(id=request.GET.get("name"))
            context = {
                "production": production
            }
            return render(request, "engineering/production.html", context)
        elif request.GET.get("edit") != None:
            production = Production.objects.get(id=request.GET.get("edit"))
            form = ProductionForm(instance=production)
            context = {
                "production": production,
                "form": form
            }
            return render(request, "engineering/production_edit.html", context)
        elif request.GET.get("add") != None:
            form = ProductionForm
            context = {
                "form": form
            }
            return render(request, "engineering/production_edit.html", context)
        elif request.GET.get("delete") != None:
            Production.objects.filter(id=request.GET.get("delete")).delete()
            return HttpResponseRedirect(reverse("production"))
        else:
            productions = Production.objects.all()
            context = {
                "productions": productions
            }
            return render(request, "engineering/productions_list.html", context)
    elif request.method == "POST":
        if request.GET.get("edit") != None:
            production = Production.objects.get(id=request.GET.get("edit"))
            form = ProductionForm(data=request.POST, instance=production)
            context = {
                "production": production,
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # =====================================================================================================
                try:
                    check = Production.objects.get(name=form.cleaned_data["name"])
                except:
                    check = None
                if check and int(check.id) != int(request.GET.get("edit")):
                    context["warn_name"] = "该产品线已经存在, 产品线名称变更错误"
                    return render(request, "engineering/production_edit.html", context)
                try:
                    check = Production.objects.get(tag=form.cleaned_data["tag"])
                except:
                    check = None
                if check and int(check.id) != int(request.GET.get("edit")):
                    context["warn_tag"] = "该产品标识已经被使用, 产品线标识变更错误"
                    return render(request, "engineering/production_edit.html", context)
                # =====================================================================================================
                form.save()
                return render(request, "engineering/production.html", context)
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


# =====================================================================================================================
# project view set
# =====================================================================================================================
@login_required()
def project(request):
    if request.method == "GET":
        if request.GET.get("name") != None:
            project = Project.objects.get(id=request.GET.get("name"))
            context = {
                "project": project
            }
            return render(request, "engineering/project.html", context)
        elif request.GET.get("edit") != None:
            project = Project.objects.get(id=request.GET.get("edit"))
            form = ProjectForm(instance=project)
            context = {
                "project": project,
                "form": form
            }
            return render(request, "engineering/project_edit.html", context)
        elif request.GET.get("add") != None:
            form = ProjectForm
            context = {
                "form": form
            }
            return render(request, "engineering/project_edit.html", context)
        elif request.GET.get("delete") != None:
            pass
        else:
            projects = Project.objects.all()
            context = {
                "projects": projects
            }
            return render(request, "engineering/projects_list.html", context)
    elif request.method == "POST":
        if request.GET.get("edit") != None:
            project = Project.objects.get(id=request.GET.get("edit"))
            form = ProjectForm(data=request.POST, instance=project)
            context = {
                "project": project,
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # this is checking part
                # =====================================================================================================
                try:
                    check = Project.objects.get(full_name=form.cleaned_data["full_name"])
                except:
                    check = None
                if check and int(check.id) != int(request.GET.get("edit")):
                    context["warn_name"] = "当前工程已经存在, 工程名称变更错误"
                    return render(request, "engineering/project_edit.html", context)
                try:
                    check = Project.objects.get(full_tag=form.cleaned_data["full_tag"])
                except:
                    check = None
                if check and int(check.id) != int(request.GET.get("edit")):
                    context["warn_tag"] = "当前工程标识已经被占用, 请重新指定一个有效的工程标识"
                    return render(request, "engineering/project_edit.html", context)
                # =====================================================================================================
                form.save()
                return render(request, "engineering/project.html", context)
            else:
                return render(request, "engineering/project_edit.html", context)
        elif request.GET.get("add") != None:
            form = ProjectForm(request.POST)
            context = {
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # this is checking part
                # =====================================================================================================
                try:
                    check = Project.objects.get(full_name=form.cleaned_data["full_name"])
                except:
                    check = None
                if check:
                    context["warn_name"] = "当前工程已经存在, 请勿重复添加"
                    return render(request, "engineering/project_edit.html", context)
                try:
                    check = Project.objects.get(full_tag=form.cleaned_data["full_tag"])
                except:
                    check = None
                if check:
                    context["warn_tag"] = "当前工程标识已经被占用, 请重新指定一个有效的工程标识"
                    return render(request, "engineering/project_edit.html", context)
                # =====================================================================================================
                form.save()
                return HttpResponseRedirect(reverse("project"))
        else:
            return HttpResponseBadRequest(content="POST 错误 *** 错误定位到 engineering.views.project")
    else:
        return HttpResponseBadRequest(content="request 错误 *** 错误定位到 engineering.views.project")