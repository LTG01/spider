import fontTools

import requests

from fontTools.ttLib import TTFont
from copyheaders import headers_raw_to_dict
from selenium import webdriver
import re

# 小说url
url = 'https://maoyan.com/films/1198214'

headers = '''
Host: maoyan.com
Pragma: no-cache
Cookie: __mta=55540244.1590730449722.1590733733143.1590812338232.8; uuid_n_v=v1; uuid=3A227D80992511EA918B751F8D8D70CA4511DAEB7EDE4FC49DB5AF94FDCBC15B; mojo-uuid=44994d48ee403d6bc28ec5b4d13a4986; _lxsdk_cuid=17228a1a7f5c8-0906036a2199f8-30667d00-13c680-17228a1a7f5c8; _lxsdk=3A227D80992511EA918B751F8D8D70CA4511DAEB7EDE4FC49DB5AF94FDCBC15B; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=55540244.1590730449722.1590733790889.1590733795600.10; _csrf=25cd2bcc082dae5facba7ed469d09456d0fe3ceeefd668307c5409ef3190e257; mojo-session-id={"id":"a4c2ec6fc2bfb9320673f2581c0e49b7","time":1590812338100}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1589819582,1590730450,1590812338; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1590812338; _lxsdk_s=17263cde73b-a1e-9b4-3%7C%7C2
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
'''

headers = headers_raw_to_dict(bytes(headers, encoding="utf-8"))

response = requests.get(url, headers=headers)
response.encoding=response.apparent_encoding
text = response.text

# driver = webdriver.Chrome()
#
# driver.get(url)
# driver.implicitly_wait(20)
#
# text =driver.page_source


with open('maoyan.html', 'w', encoding='utf-8') as f:
    f.write(text)

print(text)
# format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/FUptQXVc.woff') format('woff'),
font_url = "http:"+re.findall("url\('(.*?)'\) format\('woff'\);", text)[0]
print(font_url)

name = font_url.split('/')[-1]

#
font_content = requests.get(font_url).content

with open(name, 'wb') as f:
    f.write(font_content)

font = TTFont(name)
font.saveXML('maoyan.xml')

data_dic={}
i=0
gly_list = font.getGlyphOrder()     # 获取 GlyphOrder 字段的值
for gly in gly_list[2:]:    # 前两个值不是我们要的，切片去掉
    print()
    data_dic[gly[3:].lower()]=i
    i+=1
print(data_dic)

for key ,value in data_dic.items():
    text = text.replace("&#x"+key+';',str(value))

with open('maoyan2.html', 'w', encoding='utf-8') as f:
    f.write(text)