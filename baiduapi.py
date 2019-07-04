# -*- coding: utf-8 -*-
import json
import random
import requests

key_list = [
    # 'xx', # 百度地图申请的key
]


def convert_BD09_2_MCT(lng, lat):
    """
    通过百度提供的api，将BD09(百度专用的地图经纬度)转为墨卡托坐标
    :param lng:
    :param lat:
    :return:字典格式数据 x:经度 y:纬度
    """
    url = 'http://api.map.baidu.com/geoconv/v1/?coords={},{}&from=5&to=6&ak={}'

    ak = random.choice(key_list)
    response = requests.get(url.format(lng, lat, ak))
    res = json.loads(response.text)
    if res.get('status') == 0:
        return res['result'][0]
    else:
        print('转换为墨卡托坐标失败')
        return {}


def convert_MCT_2_BD09(lng, lat):
    """
    通过百度提供的api，将墨卡托坐标转换成BD09(百度专用的地图经纬度)
    :param lng:
    :param lat:
    :return:
    """
    url = 'http://api.map.baidu.com/geoconv/v1/?coords={},{}&from=6&to=5&ak={}'
    ak = random.choice(key_list)
    response = requests.get(url.format(lng, lat, ak))
    res = json.loads(response.text)
    if res.get('status') == 0:
        return res['result'][0]
    else:
        print('转换为经纬度坐标失败')
        return {}


if __name__ == '__main__':
    a = convert_BD09_2_MCT(116.313795, 40.074476)
    print(a['x'], a['y'])
    b = convert_MCT_2_BD09(12965500, 4842070)
    print(b['x'], b['y'])
