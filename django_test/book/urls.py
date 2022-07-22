# -*- encoding: utf-8 -*-
"""
@File    : urls.py
@Time    : 2022/7/21 5:15 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from django.urls import path  # 导入路径相关配置
from . import views  # 导入视图views

urlpatterns = [
    path('', views.index, name="index"),  # 默认访问book业务的首页
]
