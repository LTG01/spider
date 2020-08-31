#--coding:utf-8--

import requests
import execjs


word = input('输入翻译内容')
# 读取js文件
with open('tt.js', encoding='utf-8') as f:
    js = f.read()

# 通过compile命令转成一个js对象
docjs = execjs.compile(js)

# 调用function方法
tk = docjs.call('gettk',word)
print(tk)

# 调用变量方法
# res = docjs.eval('name')
# print(res)


url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&tk=225129.371558&q=python'

url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&tk=423553.45710&q=cat'



url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md{0}&q={1}'.format(tk,word)

url = 'https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=cn-ZH&hl=cn-ZH&dt=at&dt=bd&dt=ex&dt=ld&dt=md{0}&q={1}'.format(tk,word)


params={
    'client': 'webapp',
    'sl':  'auto',
    'tl': 'zh-CN',
    'hl': 'zh-CN',
    'dt': 'at',
    'dt': 'bd',
    'dt': 'ex',
    'dt': 'ld',
    'dt': 'md',

    'tk': '225129.371558',
    'q': 'python'


}
res = requests.get(url=url)
# print(res.text)
import pprint
pprint.pprint(res.json())