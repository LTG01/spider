# import random
# print(random.randint(1,5))

# t=['a','b']
# b=['t','a', 'b','c']
# for i in range(len(b)):
#     print(i,b[i])
#     if b[i] in t :
#         i+=1


import requests
import time

from lxml import etree
url='http://fund.eastmoney.com/trade/hh.html'
i=0
while 1:
    html=requests.get(url).text

    html = html.encode("ISO-8859-1")
    # html = html.encode("utf-8")
    response = etree.HTML(html)

    print(response)
    t=response.xpath('//table[@class="mainTb"]/tbody/tr')
    # t = res.css('table tbody tr').extract()
    print(len(t),t)
    for item in t:
        name = item.xpath('./td/text()|./td/a/text()|./td/span/text()')
        # tt=name[0].encode('ISO-8859-1')
        print(len(name),name)
    i+=1
    print(str(i)+'  #'*100)

    time.sleep(1)



