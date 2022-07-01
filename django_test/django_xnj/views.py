# -*- encoding: utf-8 -*-
"""
@File    : views.py
@Time    : 2022/6/18 10:27 上午
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from django.http.response import HttpResponse
from django.shortcuts import render


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse('This is first test')
    else:
        return render(request, 'login.html')
    if request.method == 'GET':
        return render(request, 'login.html')