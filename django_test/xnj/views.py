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
        password = request.POST.get('password')
        if username == 'admin' and password == '123456':
            return HttpResponse('This is first test')
    elif request.method == 'GET':
        return render(request, 'login.html')
