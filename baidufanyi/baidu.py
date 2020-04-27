import hashlib
import random
import time
import requests
import execjs

"""
向耐读翻译发送data，得到翻译结果
"""


class Youdao:
    def __init__(self, msg):
        self.url='https://fanyi.baidu.com/v2transapi'
        self.msg = msg

        if self.is_Chinese(msg):
            self.from_ = 'zh'
            self.to_ = 'en'
        else:
            self.from_ = 'en'
            self.to_ = 'zh'

    def is_Chinese(self,word):
        #判断是否为中文
        for ch in word:
            if '\u4e00' <= ch <= '\u9fff':
                return True
        return False

    def get_sign(self):
        # 进行加密
       return execjs.compile(open(r"baidu.js").read()).call('e', self.msg)

    def get_result(self):

        Form_Data = {
            'from': self.from_,
            'to': self.to_,
            'query': self.msg,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': str(self.get_sign()),
            'token': 'a55f2bfcbea8486e62478c3b266d95a2',
            'domain': 'common',

        }

        headers = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',

                    'referer': 'https://fanyi.baidu.com/?aldtype=16047',
                    'cookie': 'BIDUPSID=08219BA2BA655A070757CA06B8749638; PSTM=1586668554; BAIDUID=08219BA2BA655A07BBF869A328959A42:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=30974_1455_21126_31253_31341_31229_30823_26350_31164; delPer=0; PSINO=7; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1587133423; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1587133423; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; yjs_js_security_passport=f251a9c72164db98728e40750ab2d3b12b7adba8_1587133424_js',

                }
        response = requests.post(self.url, data=Form_Data, headers=headers)
        translate_results = response.json()
        # 找到翻译结果
        if 'trans_result' in translate_results:
            translate_results = translate_results["trans_result"]['data'][0]['dst']

            print('输入的内容是：' + self.msg)
            print("翻译后为：" + translate_results)


        else:
            print(translate_results)


def baidufanyi(keywords):
    return Youdao(keywords).get_result()



if __name__ == "__main__":
    keywords=input('输入翻译的内容：')
    baidufanyi(keywords)