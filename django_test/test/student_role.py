# -*- encoding: utf-8 -*-
"""
@File    : student_role.py
@Time    : 2022/7/15 8:51 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from http_base_lib import http_base_test, get_response_content
from students_common import Template
from student_login import post_login_user_password

token = post_login_user_password().req_data_post_login_user_password()


class get_work_moral_record(Template):
    def __init__(self, token, page, **kwargs):
        super(get_work_moral_record, self).__init__(token)
        self.method = 'GET'
        self.path = '/api/work/moral/record'
        self.query = {
            "page": page
        }
        self.status = kwargs.get('status', 200)
        self.code = kwargs.get('code', '0')
        self.data = kwargs.get('data', '*OUT*')
        self.errMsg = kwargs.get('errMsg', '*OUT*')


def req_data_get_work_moral_record(token, page, **kwargs):
    if kwargs is not None:
        get = get_work_moral_record(token, page, **kwargs)
    else:
        get = get_work_moral_record(token, page)
    request, response = get.get_data()
    http_base_test(request, response)
    return get_response_content(request)

