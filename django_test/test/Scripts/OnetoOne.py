# -*- encoding: utf-8 -*-
"""
@File    : OnetoOne.py
@Time    : 2022/4/22 11:16 上午
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""

from django_test.test.Func.sql import select_statement_all, select_execute_sql


def Teacher_student_info(role_id):
    """
    查询教师下有多少学生
    role_id:角色id
    """
    # 查询角色下拥有的教学班
    role_teach = '''SELECT permit_data-> '$[0].data.*.teachClass' AS '教学班' 
                    FROM role_data WHERE type=2 AND permit_data-> '$[0].schoolId'=1 AND id={}'''.format(role_id)
    r1 = select_execute_sql('test_school', role_teach)
    # json读取教学班id
    id = r1.get('教学班')
    # 去除数据的[]
    id = id.replace('[', '').replace(']', '')
    # 通过id查询教学班的名字
    teach_student = '''SELECT outside_id  FROM teaching_class WHERE teaching_class.id IN ({})'''.format(id)
    r2 = select_statement_all('test_school', teach_student)
    # 去除数据的[]
    outside_ids = [i['outside_id'] for i in r2]
    outside_ids = str(outside_ids).replace('[', '').replace(']', '')
    # 查询班级下的学生的信息
    student_info = '''	SELECT student_info.person_id AS '学生id',student_info.person_name AS '学生姓名' FROM 
                                calendar.student_info 
                                WHERE
                                student_info.person_id IN (SELECT
                                DISTINCT sc.person_id 
                                FROM
                                calendar.sc 
                                WHERE
                                sc.teachclass_id in ({}))'''.format(outside_ids)
    r3 = select_statement_all('calendar', student_info)
    # 通过班级id查询班级名字
    class_name = '''SELECT class_name '班级' FROM calendar.classlist WHERE id IN ({})'''.format(outside_ids)
    r4 = select_statement_all('calendar', class_name)
    # for循环打印学生信息
    # for var in r3:
    #     print(var)
    print(*r3, sep='\n')
    # 统计list下学生数量并打印总计学生
    print('当前老师班级%s' % r4, '总计学生%s人' % len(r3))


if __name__ == '__main__':
    Teacher_student_info(195)
