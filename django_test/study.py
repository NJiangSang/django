# -*- encoding: utf-8 -*-
"""
@File    : study.py
@Time    : 2022/5/11 10:17 上午
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from bs4 import BeautifulSoup
from requests import RequestException

"""使用requests模块进行网页数据爬取请求并存储到本地数据库"""
import requests
import pymysql


def get_html(url):
    """获取网页数据"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_html(html):
    """解析网页数据"""
    # 创建一个BeautifulSoup对象
    soup = BeautifulSoup(html, "html.parser")
    # 获取所有的li标签
    li_list = soup.find_all("li", class_="item")
    # 创建一个列表，用于存储数据
    data_list = []
    for li in li_list:
        # 获取每个li标签中的a标签
        a_tag = li.find("a")
        # 获取每个a标签中的href属性
        href = a_tag.get("href")
        # 获取每个a标签中的title属性
        title = a_tag.get("title")
        # 将获取的数据添加到列表中
        data_list.append(href)
        data_list.append(title)
    return data_list


"""创建数据库表如果存在则不创建"""


def create_table():
    """创建数据库表"""
    db = pymysql.connect(host="localhost", user="root", password="admin123", db="test")
    cursor = db.cursor()
    # 如果存在则不创建
    try:
        sql = "CREATE TABLE `test` (`id` int(11) NOT NULL AUTO_INCREMENT, `href` varchar(255) NOT NULL, `title` varchar(255) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;"
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()
    db.close()


"""存储网页数据到本地数据库"""


def save_data(data_list):
    """存储数据到本地数据库"""
    db = pymysql.connect(host="localhost", user="root", password="admin123", db="test")
    cursor = db.cursor()
    sql = "INSERT INTO `test` (`href`, `title`) VALUES (%s, %s)"
    cursor.executemany(sql, data_list)
    db.commit()
    db.close()


"""函数调用"""


def main():
    """主函数"""
    # 获取网页数据
    url = "http://www.xiaoyunyu.com"
    html = get_html(url)
    # 解析网页数据
    data_list = parse_html(html)
    # 存储数据到本地数据库
    create_table()
    save_data(data_list)


if __name__ == '__main__':
    main()
