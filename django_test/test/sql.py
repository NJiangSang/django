# -*- encoding: utf-8 -*-
"""
@File    : sql.py
@Time    : 2022/4/22 10:56 上午
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
@note: 数据库查询操作
"""

import pymysql

from django_test.test import config


def connect(ssid):
    """
    @note: 开始连接数据库 ，建立连接
    @param ssid: 数据库实例名
    """
    try:
        db = pymysql.connect(
            host=str(config.DB_HOST),
            port=int(config.DB_PORT),
            user=str(config.DB_USERNAME),
            password=str(config.DB_PASSWORD),
            database=ssid,
            cursorclass=pymysql.cursors.DictCursor,
            charset='utf8'
        )

        return db
    except Exception as e:
        print(e)


def select_one(ssid, TableName, ConditionName, name, Field):
    """
    @note: 查询数据库里一个值
    @param ssid: 数据库实例名
    @param TableName: 表明
    @param ConditionName: 查询条件
    @param name: 查询条件什么
    @param Field: 值的字段
    @return: 返回要取的值
    """
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cursors = db.cursor()  # dictCursor通过字段名称来获取对应的值
    sql = "SELECT * FROM  " + TableName + " WHERE " + ConditionName + "=" + "'" + name + "'"
    # print sql
    try:
        cursors.execute(sql)

        db.commit()

        results = cursors.fetchone()

        if results is not None:
            result = results[Field]

        else:
            print("****************************************【数据异常】")
            return results
        db.rollback()
        return result

    except pymysql.Error as msg:
        print("pymysql Error %d: %s" % (msg.args[0], msg.args[1]))
    cursors.close()
    db.close()


def select_all(ssid, TableName, ConditionName, name, Field):
    """
    @note: 查询数据库里多个值
    @param ssid: 数据库实例名
    @param TableName: 表明
    @param ConditionName: 查询条件
    @param name: 查询条件什么
    @param Field: 值的字段
    @return: 返回要取的值，返回值类型是list
    """
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cursors = db.cursor()  # dictCursor通过字段名称来获取对应的值
    sql = "SELECT * FROM  " + TableName + " WHERE " + ConditionName + "=" + "'" + name + "'"
    # print sql
    ress = []
    try:
        # 执行sql，通过游标来执行
        cursors.execute(sql)

        db.commit()
        # 定义个list存放获取的数据
        # 使用fetchall获取所有数据
        results = cursors.fetchall()
        # 保存为list
        result = list(results)
        # 通过list循环获取所要的字段
        for i in range(len(result)):
            # 判断不为空
            if result[i] is not None:
                # cloud_list.append(r)
                res = result[i][Field]
                ress.append(res)
                # 得到的所需要的字段，全部放到ress里面
            else:
                print("*****************************************【list为空，无数据或数据异常】")
                db.rollback()

        return ress
    except pymysql.Error as msg:
        print("【pymysql Error %d: %s】" % (msg.args[0], msg.args[1]))
    cursors.close()
    db.close()


# 直接用sql语句去表示查询
def select_statement_all(ssid, sql):
    """
    @note: 查询数据库里多个值
    @param ssid: 数据库实例名
    @param sql: sql语句
    @return: 返回要取的值，返回值类型是list

    - note:查询数据库里多个值

    Args:

        - ssid : 数据库实例名dss
        - sql : SQL语句
        - Field : 查询的字段

    Example:

        | Select Statement All | select * from| xx|

    Return: 返回要取的值，返回值类型是list

    """
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cursors = db.cursor()  # dictCursor通过字段名称来获取对应的值
    # print sql
    ress = []
    try:
        # print(sql)
        # 执行sql，通过游标来执行
        cursors.execute(sql)
        db.commit()
        # 定义个list存放获取的数据
        # 使用fetchall获取所有数据
        results = cursors.fetchall()
        # 保存为list
        result = list(results)
        # 通过list循环获取所要的字段
        for i in range(len(result)):
            # 判断不为空

            if result[i] is not None:
                # cloud_list.append(r)
                res = result[i]

                ress.append(res)
                # 得到的所需要的字段，全部放到ress里面
            else:
                print("*****************************************【list为空，无数据或数据异常】")
                db.rollback()

        return ress
    except pymysql.Error as msg:
        print("pymysql Error %d: %s" % (msg.args[0], msg.args[1]))
    cursors.close()
    db.close()


def select_statement_one(ssid, sql, Field):
    """
    @note: 查询数据库里单个值
    @param ssid: 数据库实例名
    @param sql: sql语句
    @param Field: 查询的字段
    @return: 返回要取的某个值

    - note:查询数据库里单个值

    Args:

        - ssid : 数据库实例名dss
        - sql : SQL语句
        - Field : 查询的字段


    Example:

        | Select Statement One | select * from where xxx='xx' | xx|

    Return: 返回要取的某个值

    """
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cursors = db.cursor()  # dictCursor通过字段名称来获取对应的值
    # print sql

    try:
        print(sql)
        cursors.execute(sql)

        db.commit()

        results = cursors.fetchone()

        if results is not None:
            result = results[Field]
        else:

            print("【*****************************************查询数据为空or有误】")
            return results
        db.rollback()

        return result

    except pymysql.Error as msg:
        print("pymysql Error %d: %s" % (msg.args[0], msg.args[1]))
    cursors.close()
    db.close()


def select_execute_sql(ssid, sql):
    """
    @note: 查询数据库里多个值
    @param ssid: 数据库实例名
    @param sql: 执行sql
    @return: 查询结果是什么，返回就是什么
    """
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cursors = db.cursor()  # dictCursor通过字段名称来获取对应的值
    # print sql
    try:
        cursors.execute(sql)

        db.commit()

        results = cursors.fetchone()

        db.rollback()
        return results

    except pymysql.Error as msg:
        print("pymysql Error %d: %s" % (msg.args[0], msg.args[1]))
    cursors.close()
    db.close()


def truncate(ssid, sql=None):
    db = connect(ssid)
    # 使用cursor方法去回去操作游标
    cur = db.cursor()
    # 执行语句
    cur.execute(sql)
    db.commit()  # 不能省，必须要加commit来提交到mysql中去确认执行
    # 关闭cursor和连接
    cur.close()
    db.close()
# if __name__ == '__main__':
#     R = select_statement_all("test_school",sql= '''SELECT outside_id FROM teaching_class WHERE teaching_class.id IN (58,59,60,61)''')
#     print(R)
