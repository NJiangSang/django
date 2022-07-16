# -*- encoding: utf-8 -*-
"""
@File    : student_role.py
@Time    : 2022/7/15 8:51 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from django_test.test.Base_libs.http_base_lib import http_base_test, get_response_content
from django_test.test.Base_libs.http_common import Template
from django_test.test.Controllers.student_login import req_data_post_login_user_password

token = req_data_post_login_user_password()


class get_site_grades(Template):
    def __init__(self, token, **kwargs):
        super(get_site_grades, self).__init__(token)
        self.method = 'GET'
        self.path = '/site/grades'
        self.query = {}
        self.status = kwargs.get('status', 200)
        self.code = kwargs.get('code', '0')
        self.data = kwargs.get('data', '*OUT*')
        self.errMsg = kwargs.get('errMsg', '*OUT*')


def req_data_get_work_moral_record(token, **kwargs):
    if kwargs is not None:
        get = get_site_grades(token, **kwargs)
    else:
        get = get_site_grades(token)
    request, response = get.get_data()
    http_base_test(request, response)
    return get_response_content(request)


if __name__ == '__main__':
    x = req_data_get_work_moral_record(token)
    print(x)