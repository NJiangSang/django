# -*- encoding: utf-8 -*-
"""
@File    : Ringmounting.py
@Time    : 2022/10/17 9:31 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""


def wuqi(a=0, b=0, c=0):
    wq60 = float(19.5) * a
    wq70 = 9 * b
    wq80 = 42 * c
    return wq60 + wq70 + wq80


def zhuangbei(a1=0, a2=0, a3=0):
    zb60 = float(18.5) * a1
    zb70 = 8 * a2
    zb80 = 25 * a3
    return zb60 + zb70 + zb80

    # if __name__ == '__main__':
    # a = wuqi(1, 0, 1)
    # b = zhuangbei(1, 0, 1)
    # c = a + b
    # a, b, c = map(int,input("请输入60,70,80武器各有多少,逗号隔开:").split(","))
    # print("60武器19.5,70武器9,80武器42")
    # a1, b1, c1 = map(int,input("请输入60,70,80装备各有多少,逗号隔开:").split(","))
    # print("60装备18.5,70装备8,80装备35")
    # print("武器总共{}万".format(wuqi(a, b, c)))
    # print("装备总共{}万".format(zhuangbei(a1, b1, c1,)))
    # print("共{}万".format(wuqi(a, b, c) + zhuangbei(a1, b1, c1)))
    # # print("武器总共{}万".format(a), "装备总共{}万".format(b), "总共{}万".format(c))
