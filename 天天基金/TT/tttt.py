import  requests
from copyheaders import headers_raw_to_dict

url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18304669490517963433_1589642622770&fundCode=320007&pageIndex=1&pageSize=20&startDate=&endDate=&_=1589642622808'


params={

'callback': 'jQuery183020301328783858152_1589642042716',
'fundCode': '320007',
'pageIndex': '3',
'pageSize': '20',
'startDate': '',
'endDate': '',
'_': '1589642071365',

}



headers = '''
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Cookie: EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; st_si=74886082315787; st_asi=delete
Host: api.fund.eastmoney.com
Pragma: no-cache
Referer: http://fundf10.eastmoney.com/jjjz_320007.html
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
'''
# h = bytes(headers, encoding="utf-8")
# headers = headers_raw_to_dict(h)
#
# URL = 'http://fundf10.eastmoney.com/jjjz_320007.html'
# res= requests.get(url=url).text
#
# print(res)


fundCode = '000001'
pageIndex = 1
url = 'http://api.fund.eastmoney.com/f10/lsjz'

# 参数化访问链接，以dict方式存储
params = {
    'callback': 'jQuery18307633215694564663_1548321266367',
    'fundCode': fundCode,
    'pageIndex': pageIndex,
    'pageSize': 20,
}
# 存储cookie内容
cookie = 'EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; EMFUND7=null; EMFUND8=null; EMFUND0=null; EMFUND9=01-24 17:11:50@#$%u957F%u4FE1%u5229%u5E7F%u6DF7%u5408A@%23%24519961; st_pvi=27838598767214; st_si=11887649835514'
# 装饰头文件
headers = {
    'Cookie': cookie,
    'Host': 'api.fund.eastmoney.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundCode,
}
r = requests.get(url=url, headers=headers, params=params)  # 发送请求
import pprint
pprint.pprint(r.text)