# -*- coding: utf-8 -*-


from django.shortcuts import render, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.utils.translation import ugettext_lazy as lazy
from engineering.models import Production, Project
from .forms import LoginForm, EmployeeAddForm, EmployeeEditForm, PasswordControlForm, PasswordEditForm, DepartmentForm
from .models import Employee, Department


# =====================================================================================================================
# login / logout view part
# =====================================================================================================================
def login(request):
    """
    we use the function django.contrib.auth.decorators.login_required as a decorator, if user have not login our tidal
    hunter, we need to redirect his page into login page, like this:

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


# =====================================================================================================================
# employee views part
# =====================================================================================================================
@login_required()
def employee(request):
    """
    we put all employee views input this function, it means that tidal function will just use one request path to
    control employee, and divide every func by some different parameters, like:

        * /path/to/employees/?name=<employee_id>           the readonly page of employee's information show
        * /path/to/employees/?edit=<employee_id>           the edit page of a existing employee
        * /path/to/employees/?add=True                     the adding edit page of a not existing employee
        * /path/to/employees/?delete=<employee_id>         delete one existing user and redirect page to users list
        * /path/to/employees/                              the page showing all employees by list
    """
    if request.method == "GET":
        if request.GET.get("name") != None:
            context = {
                "employee": Employee.objects.get(id=request.GET.get("name")),
                "productions": Production.objects.filter(manager=request.GET.get("name")),
                "dev_projects": Project.objects.filter(developer=request.GET.get("name")),
                "tes_projects": Project.objects.filter(tester=request.GET.get("name")),
                "ops_projects": Project.objects.filter(operator=request.GET.get("name"))
            }
            return render(request, "account/employee.html", context)
        elif request.GET.get("edit") != None:
            employee = Employee.objects.get(id=request.GET.get("edit"))
            form = EmployeeEditForm(instance=employee)
            context = {
                "employee": employee,
                "form": form
            }
            return render(request, "account/employee_edit.html", context)
        elif request.GET.get("add") != None:
            form = EmployeeAddForm
            context = {
                "form": form
            }
            return render(request, "account/employee_edit.html", context)
        elif request.GET.get("delete") != None:
            Employee.objects.filter(id=request.GET.get("delete")).delete()
            return HttpResponseRedirect(reverse("employee"))
        elif request.GET.get("password") != None:
            user = Employee.objects.get(id=request.GET.get("password"))
            form = PasswordControlForm(user=user)
            context = {
                "employee": user,
                "form": form,
                "password_errors_checking": 0
            }
            return render(request, "account/password_control.html", context)
        else:
            employees = Employee.objects.all()
            context = {
                "employees": employees
            }
            return render(request, "account/employees_list.html", context)
    elif request.method == "POST":
        if request.GET.get("edit") != None:
            employee = Employee.objects.get(id=request.GET.get("edit"))
            form = EmployeeEditForm(request.POST, instance=employee)
            context = {
                "employee": employee,
                "form": form
            }
            if form.is_valid():
                form.save()
                return render(request, "account/employee.html", context)
            else:
                return render(request, "account/employee_edit.html", context)
        elif request.GET.get("add") != None:
            form = EmployeeAddForm(request.POST)
            context = {
                "form": form
            }
            if form.is_valid():
                employee = form.save(commit=False)
                employee.set_password(form.cleaned_data.get("password"))
                employee.save()
                return HttpResponseRedirect(reverse("employee"))
            else:
                return render(request, "account/employee_edit.html", context)
        elif request.GET.get("password") != None:
            user = Employee.objects.get(id=request.GET.get("password"))
            form = PasswordControlForm(data=request.POST, user=user)
            context = {
                "employee": user,
                "form": form,
                "password_errors_checking": 0
            }
            if form.is_valid():
                form.save()
                context["password_errors_checking"] = 1
                return render(request, "account/password_control.html", context)
            else:
                return render(request, "account/password_control.html", context)
        else:
            return HttpResponseBadRequest(content="POST 错误 *** 错误定位到 account.views.employee")
    else:
        return HttpResponseBadRequest(content="request 错误 *** 错误定位到 account.views.employee")


# =====================================================================================================================
# definition of the views for the user's personal center
# =====================================================================================================================
@login_required()
def myself(request):
    if request.method == "GET":
        if request.GET.get("password") != None:
            form = PasswordEditForm(user=request.user)
            context = {
                "form": form,
                "password_errors_checking": 0
            }
            return render(request, "account/password_update.html", context)
        else:
            context = {
                "productions": Production.objects.filter(manager=request.user),
                "dev_projects": Project.objects.filter(developer=request.user),
                "tes_projects": Project.objects.filter(tester=request.user),
                "ops_projects": Project.objects.filter(operator=request.user)
            }
            return render(request, "account/myself.html", context)
    elif request.method == "POST":
        if request.GET.get("password"):
            form = PasswordEditForm(data=request.POST, user=request.user)
            context = {
                "form": form,
                "password_errors_checking": 0
            }
            if form.is_valid():
                form.save()
                context["password_errors_checking"] = 1
                return render(request, "account/password_update.html", context)
            else:
                return render(request, "account/password_update.html", context)
        else:
            return HttpResponseBadRequest(content="POST 错误 *** 错误定位到 account.views.myself")
    else:
        return HttpResponseBadRequest(content="request 错误 *** 错误定位到 account.views.myself")


# =====================================================================================================================
# department controlling views
# =====================================================================================================================
@login_required()
def department(request):
    if request.method == "GET":
        if request.GET.get("name") != None:
            department = Department.objects.get(id=request.GET.get("name"))
            context = {
                "employees": Employee.objects.filter(department=department.id),
                "employees_count": len(Employee.objects.filter(department=department.id)),
                "productions": Production.objects.filter(department=department.id),
                "productions_count": len(Production.objects.filter(department=department.id))
            }
            return render(request, "account/department.html", context)
        elif request.GET.get("edit") != None:
            department = Department.objects.get(id=request.GET.get("edit"))
            form = DepartmentForm(instance=department)
            context = {
                "department": department,
                "form": form
            }
            return render(request, "account/department_edit.html", context)
        elif request.GET.get("add") != None:
            form = DepartmentForm()
            context = {
                "form": form
            }
            return render(request, "account/department_edit.html", context)
        elif request.GET.get("delete") != None:
            department = Department.objects.get(id=request.GET.get("delete"))
            if Department.objects.filter(father=department.id):
                messages.error(request, lazy("当前部门仍然有下属机构, 删除阻止"))
                return HttpResponseRedirect(reverse("department"))
            else:
                Department.objects.filter(id=request.GET.get("delete")).delete()
                return HttpResponseRedirect(reverse("department"))
        else:
            departments = Department.objects.all()
            for department in departments:
                department.employees_count = len(Employee.objects.filter(department=department.id))
            context = {
                "departments": departments
            }
            return render(request, "account/departments_list.html", context)
    elif request.method == "POST":
        if request.GET.get("edit") != None:
            department = Department.objects.get(id=request.GET.get("edit"))
            form = DepartmentForm(data=request.POST, instance=department)
            context = {
                "department": department,
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # this is a checking part for providing a unique department full name
                # =====================================================================================================
                try:
                    check = Department.objects.get(full_name=form.cleaned_data["full_name"])
                except:
                    check = None
                if not check or int(check.id) == int(request.GET.get("edit")):
                    form.save()
                    return HttpResponseRedirect(reverse("department"))
                else:
                    context["warn_msg"] = "该部门已经存在, 请勿重复建立"
                    return render(request, "account/department_edit.html", context)
                # =====================================================================================================
            else:
                return render(request, "account/department_edit.html", context)
        elif request.GET.get("add") != None:
            form = DepartmentForm(request.POST)
            context = {
                "form": form
            }
            if form.is_valid():
                # =====================================================================================================
                # this is a checking part too
                # =====================================================================================================
                try:
                    check = Department.objects.get(full_name=form.cleaned_data["full_name"])
                except:
                    check = None
                if not check:
                    form.save()
                    return HttpResponseRedirect(reverse("department"))
                else:
                    context["warn_msg"] = "该部门已经存在, 请勿重复建立"
                    return render(request, "account/department_edit.html", context)
                # =====================================================================================================
            else:
                return render(request, "account/department_edit.html", context)
        else:
            return HttpResponseBadRequest(content="POST 错误 *** 错误定位到 account.views.department")
    else:
        return HttpResponseBadRequest(content="request 错误 *** 错误定位到 account.views.department")