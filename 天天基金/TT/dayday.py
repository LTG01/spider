import  requests
from copyheaders import headers_raw_to_dict

url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18304669490517963433_1589642622770&fundCode=320007&pageIndex=1&pageSize=20&startDate=&endDate=&_=1589642622808'
url = 'http://api.fund.eastmoney.com/f10/lsjz'

params={

# 'callback': 'jQuery183020301328783858152_1589642042716',
'fundCode': '320007',
'pageIndex': 3,
'pageSize': 20,
'startDate': '',
'endDate': '',
# '_': '1589642071365',

}



headers = '''


Host: api.fund.eastmoney.com
Referer: http://fundf10.eastmoney.com/jjjz_320007.html
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
'''
h = bytes(headers, encoding="utf-8")
headers = headers_raw_to_dict(h)

URL = 'http://fundf10.eastmoney.com/jjjz_320007.html'
res= requests.get(url=url,headers=headers,params=params).text

print(res)