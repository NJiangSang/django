# -*- encoding: utf-8 -*-
"""
@File    : http_common.py
@Time    : 2022/7/12 2:24 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import urllib.parse

from django.template.base import logger

from django_test.test.config import api_pc


def _combine_url(host, uri, query):
    """
    # 按参数组装完整的url
    :return:
    """
    base_url = "http://" + str(host) + uri
    if query is None:
        url = base_url
    else:
        if isinstance(query, dict):
            query = urllib.parse.urlencode(query)
        else:
            raise TypeError(u'query必须是字典类型')
        url = base_url + '?' + query
    return url


def get_request_data(method, path, query, body, token, header_ex, host=None, files=None):
    """
    :param method: HTTP请求的方法[]
    :param path: 请求路径的path，API中接口的路径地址。
    :param query: URL的query内容，如果有的话传，没有则为None。
    :param body: 请求的body内容，请求数据的实体内容。
    :param token: 请求鉴权token
    :param header_ex: 请求的header补充内容
    :return: 请求数据模板
    """
    if host is None:
        host = api_pc
    url = _combine_url(host, path, query)

    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate',
    }
    if token is not None:
        headers.update({'Authorization': 'Bearer ' + str(token)})
    if header_ex is not None:
        headers.update(header_ex)

    ret = {
        'method': method,
        'url': url,
        'body': body,
        'headers': headers
    }
    if files is not None:
        ret.update({"files": files})

    return ret


class Template(object):
    def __init__(self, token=None):
        self.token = token
        self.method = ''
        self.path = ''
        self.query = None
        self.body = None
        self.header = None

        # 下面是响应数据，需要根据实际情况填写，其中子类data可以不指定具体的字段，用*OUT*表示。
        self.status = ''
        self.errMsg = ''
        self.data = None

    def get_data(self):
        req_data = get_request_data(self.method, self.path, self.query, self.body, self.token, self.header)
        resp_data = {
            'status': self.status,
            'body': {
                'errMsg': self.errMsg,
                'data': self.data
            }
        }
        logger.info(u'*********************本次请求的参数*********************')
        logger.info(u'传进来的参数：Method:%s, Path:%s, Query:%s, Body:%s' % (self.method, self.path, self.query, self.body))
        logger.info(u'发送请求数据：%s' % req_data)
        logger.info(u'期望响应数据：%s' % resp_data)
        logger.info(u'******************************************************')
        return req_data, resp_data


if __name__ == '__main__':
    a = get_request_data('GET', '/v1/user/info', None, None, None,None)
    print(a)
