#--coding:

import requests

from copyheaders import headers_raw_to_dict

import parsel
import re
import pprint

cc_url= 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/0459b8acc4f8ab52744631cbdbd26ef4.svg'
#
# res = requests.get(cc_url).text

res=''
with  open('cc_tz.html','r') as f:

    res=f.read()


#
xlist = re.findall('<text x="(.*?)".*?>(.*?)</text>',res)[0]
xs = xlist[0].strip().split(' ')
xindex=[int(i) for i in xs]
value = list(xlist[1])



def getvalue(pos,xindex,value):
    for index in range(len(xindex)):
        if pos<= xindex[index]:
            return value[index]


def getvalue2(posXY, index, value):
    for xindex in range(len(index)):
        if posXY[0] <= index[xindex]:
            return value[xindex]


html_content = ''

with open('dazhong1.html','r') as f:
    html_content = f.read()


selector = parsel.Selector(html_content)

dic={
'cc': {'tz': {'tz0sl': (78.0, 26.0),
               'tz6ls': (64.0, 26.0),
               'tzh4y': (22.0, 26.0),
               'tzjs2': (8.0, 26.0),
               'tzmwx': (120.0, 26.0),
               'tzryg': (50.0, 26.0),
               'tzu2w': (134.0, 26.0),
               'tzvf1': (36.0, 26.0),
               'tzvwf': (105.0, 26.0),
               'tzwsv': (92.0, 26.0)},
        'url': 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/0459b8acc4f8ab52744631cbdbd26ef4.svg'}
}

#<cc class="tz6ls"></cc>

cc = selector.css('.phone-info cc::attr(class)').getall()
num=''
for c in cc:

    posx = dic.get('cc',{}).get('tz',{}).get(c)
    print(posx)
    key = getvalue2(posx,xindex,value)
    html_content = html_content.replace('<cc class="'+c+'"></cc>',key)
    num+=str(key)
print(num)

with open('da2.html','w') as f:
    f.write(html_content)
