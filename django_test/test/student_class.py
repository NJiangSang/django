# -*- encoding: utf-8 -*-
"""
@File    : student_class.py
@Time    : 2022/7/6 2:24 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import os

import xlsxwriter
from django_test.test.sql import select_statement_all, select_execute_sql

"""查询教学班id和班级名称"""


def Student_class(class_id):
    sql = '''SELECT id,class_name FROM `teaching_class` WHERE `id` ={} '''.format(class_id)
    r1 = select_statement_all('test_school', sql)
    print(r1)
    # 通过class_name对比课表中的班级名称
    peronid = '''SELECT person_id FROM `calendar`.`student_calendar_1_2022` WHERE `date` = '2022-07-11' AND `event_name` LIKE '{}' '''.format(
        r1[0]['class_name'])
    r2 = select_statement_all('calendar', peronid)
    # print(*r2, sep='\n')
    print(r2)
    # 写入student_class表
    for i in r2:
        student_data = '''INSERT INTO `student_class`(`person_id`, `teachclass_id`) VALUES ({},{})'''.format(
            i['person_id'], class_id)
        # r3 = select_statement_all('test_school', student_data)
        print(student_data)


'''查询班级下的学生的信息后导出本地xlsx文件'''


def Student_xlsx(class_id):
    sql = '''SELECT id,student_no,student_name FROM student_data WHERE id IN (SELECT person_id FROM `student_class` WHERE `person_id` > '473' and teachclass_id IN ({}))'''.format(
        class_id)
    r1 = select_statement_all('test_school', sql)
    # print(*r1, sep='\n')
    # 存储到xlxs文件名称带班级id,指定文件夹路径不存在则新建
    file_name = './test/student_class/{}.xlsx'.format(class_id)
    if not os.path.exists(os.path.dirname(file_name)):
        os.makedirs(os.path.dirname(file_name))
    # 创建xlsx文件
    xlsx_name = './test_xlsx/student_class_{}.xlsx'.format(class_id)
    workbook = xlsxwriter.Workbook(xlsx_name)
    worksheet = workbook.add_worksheet()
    worksheet.write_row('A1', ['id', 'student_no', 'student_name'])
    row = 1
    for i in r1:
        worksheet.write_row('A' + str(row), [i['id'], i['student_no'], i['student_name']])
        row += 1
    workbook.close()


if __name__ == '__main__':
    for i in range(68,69):
        Student_xlsx(i)
    print("done")
