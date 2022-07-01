# -*- encoding: utf-8 -*-
"""
@File    : studentno.py
@Time    : 2022/6/29 4:29 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import sys
from random import choice
import pymysql
from student_name import RandomUtil

sys.setrecursionlimit(100000)
import random


def student_no_str():
    return 10120230


'''生成随机4位数字字符串'''


def random_4_num_str():
    return random.randint(1000, 9999)


def student_no():
    return str(student_no_str()) + str(random_4_num_str())


def get_student_name():
    return RandomUtil().random_name_str('男')


def get_student_phone():
    second = [3, 4, 5, 7, 8, 9][random.randint(0, 4)]
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
        9: random.randint(0, 9)
    }[second]
    suffix = random.randint(9999999, 100000000)
    return "1{}{}{}".format(second, third, suffix)


'''更新student_no到数据库'''


def update_student_no(student_no, i):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin123', db='test', charset='utf8mb4')
    cur = conn.cursor()
    sql = "update student_data set student_no = %s where id = %s"
    cur.execute(sql, (student_no, i))
    # print(i)
    conn.commit()
    cur.close()
    conn.close()


def update_student_name(student_name, i):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin123', db='test', charset='utf8mb4')
    cur = conn.cursor()
    sql = "update student_data set student_name = %s where id = %s"
    cur.execute(sql, (student_name, i))
    conn.commit()
    cur.close()
    conn.close()


def update_student_phone(student_phone, i):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin123', db='test', charset='utf8mb4')
    cur = conn.cursor()
    sql = "update student_data set student_phone = %s where id = %s"
    cur.execute(sql, (student_phone, i))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    '''for循环生成不同的student_no、student_name'''
    for i in range(473, 10000):
        i = i + 1
        update_student_phone(get_student_phone(), i)
    # update_student_no(student_no(),i)
    # update_student_name(get_student_name(),i)

    # print('done')
