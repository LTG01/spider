import requests
import pprint
import json
url= 'http://music.taihe.com/data/tingapi/v1/restserver/ting?method=baidu.ting.song.baseInfo&songid=242078437&from=web'

url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&callback=jQuery17205602410203725166_1587571504606&songid=100575177&from=web&_=1587571536897'



url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=100575177&from=web'

url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&format=jsonp&songid=231407923&from=web'

url = 'https://link.hhtjim.com/qq/003Gy9Z03dLUPp.mp3'

headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
    # 'Referer': 'http://music.taihe.com/song/242078437',

}

# res = requests.get(url,headers=headers).text
#
# print(res)
# pprint.pprint(json.loads(res))


res= requests.get(url,headers=headers).content
with open('1.mp3','wb') as f:
    f.write(res)