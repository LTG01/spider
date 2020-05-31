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

import time

print(time.gmtime(time.time()))
print(time.localtime(time.time()))
print(time.ctime(time.time()))


