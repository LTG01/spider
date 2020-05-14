# -*- coding: utf-8 -*-
import requests
from lxml import etree
from copyheaders import headers_raw_to_dict


headers = '''
authority: music.163.com
method: GET
path: /
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6
cache-control: max-age=0
cookie: _iuqxldmzr_=32; _ntes_nnid=df5a2087ca2abb70b4bd3d6170b71dd8,1576462996114; _ntes_nuid=df5a2087ca2abb70b4bd3d6170b71dd8; WM_TID=FAq2Izmu0OhBQVVRVEdtrgGglTVpU2XD; WM_NI=Ixn8HGuhi6m6UnVf3aZbSOHiXTaPPkbaWn0cillgVZAecQsakDyUwcw%2B2U1SU2FcAMPShnFqcQcZ247MWWbO96%2B4DOE37wV%2BhJnSdG7mHVrvW4dQZSkLaSdnzu%2Blo8umOWg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d85fa59996d8b56682928eb3c85e929b9abbb825b1a9ad83b2538cedbdadf92af0fea7c3b92a8ba8a2d9cb4db7b8a7d7f03e97b29a87b26b9abe9db0cb639c8cafb1d361a2bf998fb369abb4a488d55283bbadb2f26ba99cb7b6f669b5f5feb6b45997ee8a84c447948da88fc57ba18fadbbb140f59399b8e145fbeae5d5c74587edf998d521ac96a2b4e74df5b388b7f17e95ecacb2d959a994afb4e766baabe58dee34b7b381b8e637e2a3; JSESSIONID-WYYY=Dtz2qrqubvoAeyIW1F1NCF7uF2yk3wSP%2B8Qo3jyBoIk6%2BPjP2JYn970Cc2Sf1%2Bp3%5CfFEvaoueYJmHAtnQobcm8k4hWagBqBQ4ThVZQwdennHsWMke%2Fk6vU28EqQk5uvjUvaAPCcg%2Bi7n3N4CI33dtB7cNKJ%2FkbhW9uCneafzS6i7qOfd%3A1579005850713
referer: https://music.163.com/
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'''
h = bytes(headers, encoding="utf-8")
headers = headers_raw_to_dict(h)

musicUrl_list = []
def download_parse():

    url = 'https://music.163.com/album?id=83823905'
    # datas = requests.get(url,headers=headers)
    # # sku_html = etree.HTML(datas.text)
    # print(datas.text)
    # 歌曲链接
    # url = 'https://music.163.com/album?id=83823905'

    res = requests.get(url, headers=headers)
    print(res.text)


download_parse()