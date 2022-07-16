# -*- coding: utf-8 -*-

"""

http_base_lib
最重要的底层文件，用于接口测试的http请求发送、接收、处理等操作，将响应数据同期望值比较。

"""

import json
import logging

import requests

# __all__ = ['get_response_object', 'get_response_content', 'http_base_test', 'http_export_test', 'CompareError']

response = []
http = requests.session()


def get_response_object(req=None):
    """
    :return: http request 响应的 response 对象
    """
    if req is None:
        ret = response.pop(-1)["response"]
    else:
        response_len = len(response)
        for index in range(0, response_len):
            if response[index]["req"] == req:
                ret = response.pop(index)["response"]
                break
        else:
            ret = None
    return ret


def get_response_content(req=None):
    """
    # 获取服务器的响应实体
    :return: 服务器的响应实体数据
    """
    ret = get_response_object(req)
    if ret is not None:
        return ret.json()
    else:
        return ret


status_err = 404
code_ok = 0


def http_base_test(test_data_in, except_response_data, timeout=5.0):
    """
    # 基础测试函数，测试函数入口

    :param test_data_in: 测试输入数据，数据格式{'method':'', 'url':'', 'param':'', 'token':'', 'body': ''}

    :param except_response_data: 返回数据校验，数据格式{'status':200, 'body':{}}

    :param timeout:超时时间为0，则不超时，一直运行等待。

Examples:

    | dms base test | ${test_data_in } | ${response_data} | ${timeout} |
    """
    global response

    try:
        # timeout 这个需要传递float类型
        timeout = float(timeout)
    except Exception:
        raise Exception(u'超时时间格式有误，必须是数字！ 当前的timeout =', timeout)

    resp = _send_http_request(test_data_in, timeout)
    temp_data = {"req": test_data_in, "response": resp}
    response.append(temp_data)

    # 获取请求的信息，打印使用。
    req_method = resp.request.method
    req_url = resp.request.url
    req_headers = resp.request.headers
    req_content = resp.request.body
    # print("调试打印接口返回******：{}".format(resp.content))
    # 为了将发送数据中文可以打印显示。不为空则转换。
    if req_content and type(req_content) is dict:
        req_content = json.dumps(json.loads(req_content), ensure_ascii=False)

    # 获取响应的信息，打印使用。
    resp_status = resp.status_code
    resp_reason = resp.reason
    resp_headers = resp.headers
    resp_content = resp.content
    try:
        if resp_status == status_err:
            logging.error('服务器返回错误码：{}'.format(resp_status))
        else:
            resp_content = json.loads(resp_content)

    except ValueError:
        logging.error(u'服务器真实返回：：%s' % resp_content)
        raise ValueError(u'响应的数据非JSON格式，解析出错！')

    logging.info(u'【请求行】：%s %s' % (req_method, req_url))
    logging.info(u'【请求头】：%s' % req_headers, )
    try:
        logging.info(u'【请求数据】：%s' % req_content)
    except:
        logging.error(u'【请求数据】：打印失败')

    logging.info(u'【状态行】：%s %s' % (resp_status, resp_reason))
    logging.info(u'【响应头】：%s' % resp_headers)
    try:
        logging.info(u'【响应数据】：%s' % resp_content)
    except:
        logging.error(u'【响应数据】：打印失败', )

    if resp_status == except_response_data['status']:
        if len(except_response_data['body']) == len(resp_content):
            _merge_resp_to_exp(except_response_data['body'], resp_content)
            if resp_content == except_response_data['body']:
                return 0
            else:
                logging.error(u'【用例执行结果】：【失败！】\n【用例失败原因】：【实际响应结果跟预期不符合。】')
                logging.error(u'【实际响应的实体内容】:%s' % _dict_sort(resp_content), )
                logging.error(u'【期望响应的实体内容】:%s' % _dict_sort(except_response_data['body']))
                raise CompareError
        else:
            logging.info(u'【用例执行结果】：【成功！】\n【但实际响应结果跟预期字段不符合。】')
    else:
        logging.error(u'【用例执行结果】：【失败！】\n【用例失败原因】：【实际响应状态码跟预期不符合。】')
        logging.error(u'【实际响应的状态码为】:%s' % resp_status, )
        logging.error(u'【期望响应的状态码为】:%s' % except_response_data['status'])
        raise StatusCompareError


def _send_http_request(test_data, timeout=5.0):
    """

    # 依据基础的http请求数据，发送http请求

    :param test_data: http请求的数据, 数据格式

    :return: Response对象

    """
    # host1 = vg.CLIENT_HOST, port1 = vg.CLIENT_PORT
    method = test_data['method']
    url = test_data['url']
    body = test_data['body']
    headers = test_data['headers']
    method = method.upper()
    if method == 'HEAD':
        resp = http.request('HEAD', url, json=body, headers=headers, timeout=timeout)

    elif method == 'GET':
        resp = http.request('GET', url, json=body, headers=headers, timeout=timeout)

    elif method == 'POST':
        resp = http.request('POST', url, json=body, headers=headers, verify=False, timeout=timeout)

    elif method == 'PUT':
        resp = http.request('PUT', url, json=body, headers=headers, timeout=timeout)

    elif method == 'DELETE':
        resp = http.request('DELETE', url, json=body, headers=headers, timeout=timeout)
    else:
        raise Exception(u'请求类型错误！当前请求的类型为：%s' % method)

    return resp


def _merge_resp_to_exp(exp_data, resp_data):
    """
    对期望值与实际的返回值，做处理，方便对比；当期望值写入*OUT*，将采用实际返回值做替换
    """
    try:
        for i in exp_data:  # 遍历所有元素
            if isinstance(exp_data[i], list):
                for j in range(0, len(exp_data[i])):  # 遍历数组，如果存在元素不是dict，进行排序
                    if not isinstance(exp_data[i][j], dict):
                        exp_data[i].sort()
                        resp_data[i].sort()
                        break
                for j in range(0, len(exp_data[i])):  # 遍历该数组所有值
                    if isinstance(exp_data[i][j], dict):  # 如果是字典
                        _merge_resp_to_exp(exp_data[i][j], resp_data[i][j])
                    elif isinstance(exp_data[i][j], list):  # 如果是列表
                        _merge_resp_to_exp(exp_data[i][j], resp_data[i][j])
                    else:
                        if exp_data[i][j] == '*OUT*':
                            exp_data[i][j] = resp_data[i][j]
            if isinstance(exp_data[i], dict):
                _merge_resp_to_exp(exp_data[i], resp_data[i])
            if exp_data[i] == '*OUT*':
                exp_data[i] = resp_data[i]
    except TypeError:
        print(u'字典里面的键值比较出现错误，请检查期望结果跟实际响应数据。大概率是期望数据没有传正确导致。')
    return 0


def _dict_sort(input_data, use_dumps=True):
    """
    # 字典数据排序，针对有些键值对应的有list，且list里面又包含了dict的时候，多了一步处理，使得最终打印出来都是中文。
    """
    if isinstance(input_data, dict):
        for i in input_data:
            if isinstance(input_data[i], (dict, list)):
                _dict_sort(input_data[i], use_dumps=False)
        if use_dumps:
            input_data = json.dumps(input_data, sort_keys=True, ensure_ascii=False)

        # 不需要转换的是有嵌套的时候，内部排序好后，最后再一次性的转换。
        else:
            input_data = json.loads(json.dumps(input_data, sort_keys=True), encoding='utf-8')

    if isinstance(input_data, list):
        for i in range(0, len(input_data)):
            input_data[i] = _dict_sort(input_data[i], use_dumps=False)
    return input_data


# def http_export_test(test_data_in, except_response_data=None, timeout=5.0):
#     """
#     # 改造http_base_test方法。适用于导出文件操作。
#     正常业务导出except_response_data不需要传入。
#     异常测试时需要传入except_response_data。封装Template时，建议如下：
#         self.status = kwargs.get('status', 200)
#         self.code = kwargs.get('code',  '*OUT*')
#         self.data = kwargs.get('data', '*OUT*')
#         self.errMsg = kwargs.get('errMsg', '*OUT*')
#         self.success = kwargs.get('success', False)
#
#     :param test_data_in: 测试输入数据，数据格式{'method':'', 'url':'', 'param':'', 'token':'', 'body': ''}
#
#     :param except_response_data: 返回数据校验，数据格式{'status':200, 'body':{}}
#
#     :param timeout:超时时间为0，则不超时，一直运行等待。
#
# Examples:
#
#     | dms base test | ${test_data_in } | ${timeout} |
#     """
#     global response
#
#     try:
#         # timeout 这个需要传递float类型
#         timeout = float(timeout)
#     except Exception:
#         raise Exception(u'超时时间格式有误，必须是数字！ 当前的timeout =', timeout)
#
#     resp = _send_http_request(test_data_in, timeout)
#     temp_data = {"req": test_data_in, "response": resp}
#     response.append(temp_data)
#
#     # 获取请求的信息，RF打印使用。
#     req_method = resp.request.method
#     req_url = resp.request.url
#     req_headers = resp.request.headers
#     req_content = resp.request.body
#     # 为了将发送数据中文可以打印显示。不为空则转换。
#     if req_content and type(req_content) is dict:
#         req_content = json.dumps(json.loads(req_content), ensure_ascii=False)
#
#     # 获取响应的信息，RF打印使用。
#     resp_status = resp.status_code
#     resp_headers = resp.headers
#     resp_content = resp.content
#     if resp_status == status_err:
#         raise ValueError(u'服务器返回错误码：\n' + str(resp_status))
#     try:
#         if except_response_data is not None:
#             resp_content = resp.json()
#             if resp_status == except_response_data['status']:
#                 if len(except_response_data['body']) == len(resp_content):
#                     _merge_resp_to_exp(except_response_data['body'], resp_content)
#
#                     if resp_content == except_response_data['body']:
#                         return 0
#
#                     else:
#                         logging.info(u'【用例执行结果】：【失败！】\n【用例失败原因】：【实际响应结果跟预期不符合。】')
#                         logging.info(u'【实际响应的实体内容】:%s' % _dict_sort(resp_content), )
#                         logging.info(u'【期望响应的实体内容】:%s' % _dict_sort(except_response_data['body']))
#                         raise CompareError
#                 else:
#                     logging.info(u'【用例执行结果】：【成功！】\n【但实际响应结果跟预期字段不符合。】')
#
#             else:
#                 logging.info(u'【用例执行结果】：【失败！】\n【用例失败原因】：【实际响应状态码跟预期不符合。】')
#                 logging.info(u'【实际响应的实体内容】:%s' % _dict_sort(resp_content))
#                 logging.info(u'【实际响应的状态码为】:%s' % resp_status)
#                 logging.info(u'【期望响应的状态码为】:%s' % except_response_data['status'])
#                 raise CompareError
#
#     except ValueError:
#         raise ValueError(u'响应的数据解析出错！')
#
#     logging.info(u'【请求行】：%s %s' % (req_method, req_url))
#     logging.info(u'【请求头】：%s' % req_headers)
#     try:
#         logging.info(u'【请求数据】：%s' % (req_content[:2048]))
#     except:
#         logging.info(u'【请求数据】：打印失败')
#
#     logging.info(u'【状态行】：%s ' % resp_status)
#     logging.info(u'【响应头】：%s' % resp_headers)


class CompareError(Exception):
    pass


class StatusCompareError(Exception):
    pass
