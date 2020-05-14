from chaojiying_Python.chaojiying import *

import requests

from lxml import etree

session = requests.Session()
#登陆界面url

headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
'referer': 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx',
}

loginUrl='https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

response = session.get(loginUrl).text
html=etree.HTML(response)

imgUrl='https://so.gushiwen.org/'+html.xpath('//*[@id="imgCode"]/@src')[0]
print(imgUrl)

img=session.get(imgUrl).content

with open('code.jpg','wb') as f:
    f.write(img)

chaojiying = Chaojiying_Client('yiqieanran01', 'chaojiying1qazxsw2', '904611')  # 用户中心>>软件ID 生成一个替换 96001
im = open('code.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
code=chaojiying.PostPic(im, 1902)['pic_str']

# print(chaojiying.PostPic(im, 1902))
print(code)
data={

'__VIEWSTATE': '7eVp9YqwCbSU687x/bxyiZttdI+RJojHGUJuz7CD26CErpjIEfrpRqrQLISJAqXbSW4umLo4Ku2SIFG2Vi1n/xFOqMFGz3B+J0NEL7cAFxHuYggG0y/CpcMzcLU==',
'__VIEWSTATEGENERATOR': 'C93BE1AE',
'from': 'http://so.gushiwen.org/user/collect.aspx',
'email': '1025300573@qq.com',
'pwd':' gushiwang1qazxsw2',
'code': str(code),
'denglu': '登录'
}
print(data)

url='https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
res=requests.post(url,data=data,headers=headers).text
with open('login.html','w',encoding='utf-8') as f:
    f.write(res)