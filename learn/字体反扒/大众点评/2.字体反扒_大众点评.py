import fontTools

import requests

from fontTools.ttLib import TTFont
from copyheaders import headers_raw_to_dict

import re
from PIL import Image, ImageFont, ImageDraw
import numpy

# 小说url
url = 'http://www.dianping.com/shop/22314796'

headers = '''
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Cookie: _lxsdk_cuid=1725e53898cc8-00a56221c9380d-1b386257-13c680-1725e53898dc8; _lxsdk=1725e53898cc8-00a56221c9380d-1b386257-13c680-1725e53898dc8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1590720433; _hc.v=ccc1d798-4f6d-50c4-d97b-3014a6707c85.1590720433; lgtoken=03b3f6a74-b893-46ba-a633-151609c7f68b; dplet=44ebdbaf1374446b79f584f3b3e0a3ea; dper=89f7587fe06f9b5a8127a798f3054d4e53e310e3d97392ae9d1cb4e6ec9fd2220296ffb08024e52137c90d24797d02b200ac2e1a2bc4c2fcbb7ae65522d6c966f01a276961001386332b0d9e0c0e25983b3d8e9692d22dde7b66f6f44932ccb1; ll=7fd06e815b796be3df069dec7836c3df; ua=%E9%80%86%E6%B5%81%E8%80%8C%E4%B8%8A_2962; ctu=fe900529419a03962c38d2c1153046d0867bdba9b652361c8b54a18a3abc6755; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1590720570; _lxsdk_s=1725e53898d-b38-ab0-c11%7C%7C41
'''

headers = headers_raw_to_dict(bytes(headers, encoding="utf-8"))

response = requests.get(url, headers=headers)
text = response.text
with open('1.html', 'w', encoding='utf-8') as f:
    f.write(text)


css_url='http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/1ee0530c945b510b2d91667bf4bd4ab4.css'

css_res = requests.get(css_url).text

print(css_res)

'''@font-face {font-family: "PingFangSC-Regular-review";src: url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/2bb1bd8a.eot");'''


m= '''@font-face \{font-family: "PingFangSC-Regular-review";src: url\("(.*?).eot"\);'''

# format('eot'); src: url('https://qidian.gtimg.com/qd_anti_spider/FUptQXVc.woff') format('woff'),
font_url = 'http:'+re.findall('PingFangSC-Regular-review";src:url\("(.*?)eot"', css_res)[0]+'woff'
print(font_url)

name = font_url.split('/')[-1]

print(name)
font_content = requests.get(font_url).content

with open(name, 'wb') as f:
    f.write(font_content)

font = TTFont(name)
font.saveXML('11.xml')

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# 打开文件
font = TTFont(name)
# 获取字体编码（特殊的编码）
code_list = font.getGlyphOrder()[2:]
print(code_list)

"""逆向部分,将特殊字体绘制到一张图片上去"""
# 新建一张图片
im = Image.new("RGB", (1800, 1800), (255, 255, 255))
# 绘制图片的对象
image_draw = ImageDraw.Draw(im)
# 绘制图片中, 显示的字体
font = ImageFont.truetype(name, 40)

count = 15
# 将特殊编码等分为15分
array_list = numpy.array_split(code_list, count)

for i in range(len(array_list)):
    print('替换之前的', array_list[i])
    # 将js的unicode码转化为python的unicode
    new_list = [i.replace("uni", "\\u") for i in array_list[i]]
    print('替换之后的', new_list)

    # 将列表变为字符串
    text = "".join(new_list)
    print('列表变字符串', text)
    # text = text.encode('utf-8').decode('utf-8')
    # print(text)
    # encode decode
    # 把文字变成二进制
    # 将字符串进行反向编码
    text = text.encode('utf-8').decode('unicode_escape')
    print('反向编码之后的', text)
    # 将文件绘制到图片
    # 指定字体进行绘制
    image_draw.text((0, 100 * i), text, font=font, fill="#000000")

im.save("sss.jpg")  # 可以将图片保存到本地，以便于手动打开图片查看
im.show()


# result = pytesseract.image_to_string(im, lang="chi_sim")
# print(result)
# # # 去除空白及换行
# result_str = result.replace(" ", "").replace("\n", "")
# # 将内容替换成网页的格式，准备去网页中进行替换
# print(code_list)
# html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]
# print(html_code_list)
# map_dict = dict(zip(html_code_list, list(result_str)))
# print(map_dict)
#
# with open('替换之前.html', mode='r', encoding='utf-8') as f:
#     text = f.read()
#
# for key, value in map_dict.items():
#     print(key, value)
#     text = text.replace(key, value)
#
# with open('替换之后.html', mode='w', encoding='utf-8') as f:
#     f.write(text)





