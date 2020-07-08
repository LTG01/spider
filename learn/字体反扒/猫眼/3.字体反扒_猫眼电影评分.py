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
Cookie: __mta=42774938.1593328038201.1593328038201.1593328038201.1; uuid_n_v=v1; uuid=00085C10B90E11EAB7FDDF490BC946C0E2E06F92167A4125A92D464DDF59C9C0; _csrf=495c019624927f42d0fb3ec8dc82b5a47d0d68e2c2abd63c6e1ee7fde52d8a3e; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593328037; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593328037; _lxsdk_cuid=172f9c070a4c8-0d4066f587176d-7a1437-fa000-172f9c070a4c8; _lxsdk=00085C10B90E11EAB7FDDF490BC946C0E2E06F92167A4125A92D464DDF59C9C0; mojo-uuid=8e30e35384d695c8d4e088634a356079; mojo-session-id={"id":"3d59fceece80b850608bfeb7a06e7e64","time":1593328038124}; mojo-trace-id=1; _lxsdk_s=172f9c070a6-355-7ed-271%7C%7C2
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