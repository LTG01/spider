#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 17:00
# @Author  : ZhangYuge
# @File    : translate_yd.py

import hashlib
import random
import time
import requests

"""
向有道翻译发送data，得到翻译结果
"""
class Youdao:
    def __init__(self, msg):
        self.url = 'http://fanyi.youdao.com/translate'
        self.msg = msg
        self.ts=self.get_ts()
        self.salt=self.get_salt()
        if self.is_Chinese(msg):
            self.from_ = 'zh-CHS'
            self.to_ = 'en'
        else:
            self.from_ = 'en'
            self.to_ = 'zh-CHS'

    def is_Chinese(self, word):
        # 判断是否为中文
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False


    def get_ts(self):
        # 根据当前时间戳获取ts参数
        s = int(time.time() * 1000)
        return str(s)

    def get_salt(self):
        # 根据当前时间戳获取salt参数
        s = int(time.time() * 1000) + random.randint(0, 10)
        return str(s)

    def get_sign(self):
        # 使用md5函数和其他参数，得到sign参数
        words = "fanyideskweb" + self.msg + self.salt + "n%A-rKaT5fb[Gy?;N5@Tj"

        # 对words进行md5加密
        hashlib.md5()
        m = hashlib.md5()
        m.update(words.encode('utf-8'))
        return m.hexdigest()

    def get_result(self):
        Form_Data = {
            'i': self.msg,
            'from': self.from_,
            'to': self.to_,
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            # 'salt': self.salt,
            # 'sign': self.get_sign(),
            # 'ts': self.ts,
            'bv': 'a4f4c82afd8bdba188e568d101be3f53',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION'
        }

        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1389460813@123.125.1.12',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        response = requests.post(self.url, data=Form_Data, headers=headers)
        translate_results = response.json()
        # 找到翻译结果
        if 'translateResult' in translate_results:
            translate_results = translate_results['translateResult'][0][0]['tgt']

            print('输入的内容是：' + self.msg)
            print("翻译后为：" + translate_results)
        else:
            print(translate_results)

def youdaofanyi(keywords):
    return Youdao(keywords).get_result()


if __name__ == "__main__":
    while 1:
        keywords=input('输入翻译的内容：')
        youdaofanyi(keywords)
