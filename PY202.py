#
# m
# m=[]
# while 1:
#     line = input('输入人员信息：')
#     if line.strip() =="":
#         if len(m)==0:
#             print('没有人员信息')
#         else:
#             try:
#                 age = [int(i.split(' ')[-1]) for i in m]
#                 sex = [i.split(' ')[1] for i in m]
#                 av = format(sum(age)/len(age),'.2f')
#                 num = sex.count('男')
#                 print('平均年龄是{} 男性人数是{}'.format(av,num))
#             except Exception as e:
#                 print('数据异常')
#         break
#     m.append(line.strip())
#     # print(line)

import jieba

s = r'''中国特色社会主义进入新时代，我国社会主义主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾。'''

a=jieba.lcut(s)
n = len(a)
m = len([i for i in list(set(a)) if len(i)>1])

print('中文字符数为{},中文词语书为{}'.format(n,m))
#
# a=['今天', '我们', '中出', '了', '一个', '叛徒', '，', '不想', '领导', '领导', '的', '领导', '不是', '好', '领导']
#
#
#
#
# a=list(set(a))
# print(a,len(a))
#
# b= [i for i in a if len(i)>1]
#
# print(b,len(b))
















