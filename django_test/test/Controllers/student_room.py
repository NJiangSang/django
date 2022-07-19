# -*- encoding: utf-8 -*-
"""
@File    : student_room.py
@Time    : 2022/7/19 3:21 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""

from django_test.test.Base_libs.http_base_lib import http_base_test, get_response_content
from django_test.test.Base_libs.http_common import Template
from django_test.test.Controllers.student_login import req_data_post_login_user_password

token = req_data_post_login_user_password()


class post_add_classroom(Template):
    """新增教室"""
    def __init__(self, token, classroom_name, **kwargs):
        super(post_add_classroom, self).__init__(token)
        self.method = 'POST'
        self.path = '/classroom/add'
        self.body = {"school_id": '4',
                     "buliding_id": '9',
                     "storey": '5',
                     "classroom_name": classroom_name,
                     "max_number": 40
                     }
        self.status = kwargs.get('status', 200)
        self.code = kwargs.get('code', '0')
        self.data = kwargs.get('data', '*OUT*')
        self.errMsg = kwargs.get('errMsg', '*OUT*')


def req_data_post_add_classroom(token, classroom_name, **kwargs):
    if kwargs is not None:
        post = post_add_classroom(token, classroom_name, **kwargs)
    else:
        post = post_add_classroom(token, classroom_name)
    request, response = post.get_data()
    http_base_test(request, response)
    return get_response_content(request)


class post_add_administration(Template):
    """修改行政班班主任"""
    def __init__(self, token, id, class_name, **kwargs):
        super(post_add_administration, self).__init__(token)
        self.method = 'POST'
        self.path = '/administration/add'
        self.body = {"administrative_type_id": "1",
                     "class_room_id": ["9", "5", id],
                     "teacher_id": ["324"],
                     "grade_id": "4",
                     "class_name": class_name,
                     "school_id": "4",
                     "people_min": 1,
                     "people_max": 40
                     }
        self.status = kwargs.get('status', 200)
        self.code = kwargs.get('code', '0')
        self.data = kwargs.get('data', '*OUT*')
        self.errMsg = kwargs.get('errMsg', '*OUT*')


def req_data_post_add_administration(token, id, class_name, **kwargs):
    if kwargs is not None:
        post = post_add_administration(token, id, class_name, **kwargs)
    else:
        post = post_add_administration(token, id, class_name)
    request, response = post.get_data()
    http_base_test(request, response)
    return get_response_content(request)
