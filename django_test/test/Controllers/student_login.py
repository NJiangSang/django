# -*- encoding: utf-8 -*-
"""
@File    : student_login.py
@Time    : 2022/7/11 10:49 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""

from django_test.test.Base_libs.http_base_lib import http_base_test, get_response_content
from django_test.test.Base_libs.http_common import Template
from django_test.test.config import *

'''封装登录方法'''


class post_login_user_password(Template):
    def __init__(self, username, password, login_type, **kwargs):
        super(post_login_user_password, self).__init__()
        self.method = 'POST'
        self.path = '/auth/login'
        if login_type == 3:
            self.body = {
                'username': username,
                'password': password,
                'login_type': 3,
                "wx_unionid": username
            }
        else:
            self.body = {
                'username': username,
                'password': password,
                'login_type': login_type
            }
        self.status = kwargs.get('status', 200)
        self.code = kwargs.get('code', '0')
        self.data = kwargs.get('data', '*OUT*')
        self.errMsg = kwargs.get('errMsg', '*OUT*')


def req_data_post_login_user_password(username=username, password=password, login_type=login_type, kwargs=None):
    if kwargs is not None:
        post = post_login_user_password(username, password, login_type, **kwargs)
    else:
        post = post_login_user_password(username, password, login_type)
    request, response = post.get_data()
    http_base_test(request, response)
    token = get_response_content(request).get('data').get('token')
    return token


if __name__ == '__main__':
    x = req_data_post_login_user_password('18190947413', '80230000', 2)
    print(x)
