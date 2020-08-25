# import jieba
#
# s = r'''中国特色社会主义进入新时代，我国社会主义主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。'''
#
# a=jieba.lcut(s)
# n = len(a)
# m = len([i for i in list(set(a)) if len(i)>1])
#
# print('中文字符数为{},中文词语书为{}'.format(n,m))



# x=((3**4+5+6**7)/8)**0.5
# print(x)

# import time
#
# print(time.gmtime(time.time()))
# print(time.localtime(time.time()))
# print(time.ctime(time.time()))

import requests

#
# url = ''
#
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36"
# headers = {'User-Agent': user_agent}
#
# res = requests.get(url,headers=headers)
# print(res.status_code)

tt= 'https://www.dianping.com/shop/H68wP1TJZ14FMtav/review_all/p13'

# if tt.__contains__('review_all'):
#     k =tt.find('review_all')
#     print('s',tt[:k+10])
import re
tt = 'https://www.dianping.com/shop/k8tp0BzbK5tYyt32/review_all/p4'

index = re.match('(https://www.dianping.com/shop/[a-zA-Z0-9]+/)',tt).group(0)
print(index)