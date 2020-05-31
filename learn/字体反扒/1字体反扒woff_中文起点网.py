
import fontTools

import requests

from fontTools.ttLib import TTFont
from copyheaders import headers_raw_to_dict

import re
#小说url
url='https://book.qidian.com/info/1020133369'

headers='''
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
'''

headers = headers_raw_to_dict(bytes(headers, encoding="utf-8"))

response = requests.get(url,headers=headers)
text= response.text
with open('1.html','w',encoding='utf-8') as f:
    f.write(text)

#format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/FUptQXVc.woff') format('woff'),
font_url=re.findall("format\('eot'\); src: url\('(.*?)'\) format\('woff'\),",text)[0]
print(font_url)

name=font_url.split('/')[-1]

#
font_content = requests.get(font_url).content

with open(name,'wb') as f:
    f.write(font_content)

font= TTFont(name)
font.saveXML('1.xml')


# font_names=font.getGlyphNames()
#
# print(font_names)
#
# print(font.getGlyphNames2())
#
# print(font.getGlyphID('period'))
#
# my_dic=font.getReverseGlyphMap()
#
# print(my_dic)
map_str_2_number = {
    'period': '.',
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}




font_value=font.getBestCmap()
print(font_value)

for key in font_value.keys():

    font_value[key]=map_str_2_number[font_value[key]]

print(font_value)

for key,value in font_value.items():
    text =text.replace("&#"+str(key)+";",str(value))

with open('2.html','w') as f:
    f.write(text)
    





