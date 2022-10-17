# -*- encoding: utf-8 -*-
"""
@File    : Ringmounting.py
@Time    : 2022/10/17 9:31 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""


def wuqi(a, b, c):
    wq60 = float(19.5) * a
    wq70 = 9 * b
    wq80 = 42 * c
    return wq60 + wq70 + wq80


def zhuangbei(a1, a2, a3):
    zb60 = float(18.5) * a1
    zb70 = 8 * a2
    zb80 = 25 * a3
    return zb60 + zb70 + zb80


if __name__ == '__main__':
    print("武器总共{}万".format(wuqi(1, 1, 1)), "装备总共{}万".format(zhuangbei(1, 1, 1)))
