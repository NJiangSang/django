# -*- encoding: utf-8 -*-
"""
@File    : KPLhero.py
@Time    : 2022/7/25 9:34 AM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
import requests as r
import json

# 导入相关库

while True:  # 建立死循环，否则查询一次后会退出程序
    hero = input("输入需要查询的英雄:")  # 输入查询的英雄
    if hero == "":  # 判断输入的字符串是否是空的
        print("您输入无效\n")
        continue
    platform = input("输入需要的端是安卓还是苹果，请直接输入安卓或苹果:")
    if platform != "安卓" and platform != "苹果":  # 查询端只有安卓和苹果
        print("您输入的端无效\n")
        continue
    # 将用户输入的安卓和苹果转换为android和ios
    if platform == "安卓":
        platform = "android"
    else:
        platform = "ios"
    area = input("输入需要的大区是qq还是wx，请直接输入qq或wx:")
    if area != "qq" and area != "wx":  # 查询大区只有qq和wx
        print("您输入的大区无效\n")
        continue
    else:
        print("查询中……")
        source = r.get("https://api.fuxi.info/wz/select.php?hero=%s&platform=%s&area=%s" % (hero, platform, area)).text
        # get获取，hero英雄，platform为安卓或苹果，area为qq或微信
        _json: object = json.loads(source)
        # 返回json格式，转换为字典
        if _json["code"] == 200:
            # code为200，表示返回正常，其余数值则错误
            title = _json["data"]["name"]  # 英雄名称
            printText = ("英雄:%s\n" % title)

            area = _json["data"]["area"]  # 区名称
            areaPower = _json["data"]["areaPower"]  # 区最低战力
            printText += ("县/区:%s(%s)\n" % (area, areaPower))

            city = _json["data"]["city"]
            cityPower = _json["data"]["cityPower"]
            printText += ("市:%s(%s)\n" % (city, cityPower))

            province = _json["data"]["province"]
            provincePower = _json["data"]["provincePower"]
            printText += ("省:%s(%s)\n" % (province, provincePower))

            updatetime = _json["data"]["updatetime"]
            printText += ("更新时间:%s\n" % (updatetime))

            print(printText)
        else:
            print("查询失败\n")
            # print("错误代码：%s %s" % (_json["code", _json["msg"]))
if __name__ == '__main__':
    pass
