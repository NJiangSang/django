# -*- encoding: utf-8 -*-
"""
@File    : studentno.py
@Time    : 2022/6/29 4:29 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import sys
import pymysql
from django_test.test.Scripts.student_name import RandomUtil

sys.setrecursionlimit(100000)
import random


def student_no_str():
    return 1012025


'''生成随机4位数字字符串'''


def random_5_num_str():
    return random.randint(10000, 99999)


def student_no():
    return str(student_no_str()) + str(random_5_num_str())


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


def insert_account_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin123', db='test', charset='utf8mb4')
    cur = conn.cursor()
    cur.execute("select id from student_data")
    i = cur.fetchall()
    for r in i:
        print(r[0])
        a = "INSERT INTO `account_data`( `username`, `password`, `name`, `status`, `userid`, `dd_unionid`, `wx_unionid`, " \
            "`openid`, `remember_token`, `access_token`, `gender`, `school`, `roles`, `grade`, `student_id`, " \
            "`students_no`, `id_card`, `mobile`, `teacher_id`, `th_num`, `current_role`, `allowance`, " \
            "`allowance_updated_at`, `department`, `jobsname`, `ldapstrtus`, `role_type`, `logged_at`, `creator`, " \
            "`created_at`, `updated_at`, `is_deleted`) VALUES ('{}', " \
            "'$2y$13$8W6BD.S0zqsB2lMi3A55veKJUpf8Y7o09RnBfG5fdkbEXy1hT2S2y', '{}', 1, 'eL3220OgH1ZTc5UQsc46OPBMdCh4nKrq', " \
            "'', '', '', '', '', 0, '4', '[\"110\"]', 4, {}, '{}', '{}', '{}', 0, 0, 110, 0, 0, '', '', 0, 1, " \
            "'2022-06-30 08:54:54', 'admin', '2022-03-25 02:25:18', '2022-06-30 08:54:54', 0);".format(r[0], r[0], r[0],
                                                                                                       r[0], r[0], r[0])
        cur.execute(a)
    conn.commit()
    cur.close()
    conn.close()


def update_account_data():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin123', db='test', charset='utf8mb4')
    cur = conn.cursor()
    sql = "update account_data set students_no = %s where student_id = %s"
    cur.execute("select id,student_no from student_data")
    i = cur.fetchall()
    for r in i:
        print(r[1], r[0])
        cur.execute(sql, (str(r[1]), r[0]))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    '''for循环生成不同的student_no、student_name'''
    # for i in range(473, 10000):
    # i = i + 1
    #     update_student_phone(get_student_phone(), i)
    #     update_student_no(student_no(),i)
    #     update_student_name(get_student_name(),i)
    # print('done')
    update_account_data()
