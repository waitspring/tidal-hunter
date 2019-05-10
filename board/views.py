#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
board.views

this page includes tidal hunter's dash board views that as our website index path
"""


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# ===========================================================================================================
# dash board views set
# ===========================================================================================================
@login_required()
def board(request):
    """
    in every view function, we need to construct some context tags so that we can use these in html5 pages,
    but django has constructed a class value named requested for us, we can use it in html5 pages directly

    class request includes many attributes, like:

        * request.scheme               请求的协议, http 或是 https
        * request.path                 请求的路由, 不包括请求中的域名
        * request.path_info            具有 url 扩展名资源的附加路径信息
        * request.method               请求的方法, GET / POST / ...
        * request.content_type         请求的 mime 类型, 仅 django 1.10 及以后版本支持
        * request.content_params       请求的键值对参数, 类型为字典
        * request.GET                  请求的 GET 相关参数
        * request.POST                 请求的 POST 相关参数
        * request.META                 请求头信息构成的字典
        * request.user                 当前登录用户的信息, 使用 django.contrib.auth.models 数据模型或是我们自己定义
                                       的数据模型

    """
    return render(request, "board/board.html")