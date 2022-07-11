# -*- encoding: utf-8 -*-
"""
@File    : student_login.py
@Time    : 2022/7/11 10:49 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import logging

import requests
import config

'''封装登录方法'''


class Pc_login:
    def __init__(self):
        self.url = config.prod_api_pc + 'auth/login'
        self.username = config.prod_username
        self.password = config.prod_password
        self.login_type = config.login_type
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def login(self):
        if self.login_type == 4:
            data = {
                'username': self.username,
                'password': self.password,
                'login_type': 4,
                "wx_unionid": "18190947413"
            }
        else:
            data = {
                'username': self.username,
                'password': self.password,
                'login_type': self.login_type
            }
        r = requests.post(self.url, json=data, headers=self.headers)
        # 判断异常响应r为空时
        if r.status_code == 500:
            logging.error('登录失败，请检查网络')
        else:
            token = r.json()['data']['token']
        return token
