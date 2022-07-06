# -*- encoding: utf-8 -*-
"""
@File    : student_class.py
@Time    : 2022/7/6 2:24 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""

from django_test.test.sql import select_statement_all, select_execute_sql

"""查询教学班id和班级名称"""


def Student_class(class_id):
    id = '''SELECT id,class_name FROM `teaching_class` WHERE `id` ={} '''.format(class_id)
    r1 = select_statement_all('test_school', id)
    # print(r1)
    #通过class_name对比课表中的班级名称
    peronid = '''SELECT person_id FROM `calendar`.`student_calendar_1_2022` WHERE `date` = '2022-07-11' AND `event_name` LIKE '{}' '''.format(r1[0]['class_name'])
    r2 = select_statement_all('calendar', peronid)
    # print(*r2, sep='\n')
    # print(r2)
    #写入student_class表
    for i in r2:
        student_data = '''INSERT INTO `student_class`(`person_id`, `teachclass_id`) VALUES ({},{})'''.format(i['person_id'],class_id)
        r3 = select_statement_all('test_school', student_data)
        print(r3)

if __name__ == '__main__':
    print("done")


