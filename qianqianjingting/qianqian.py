from lxml import etree

import requests

# url='https://blog.csdn.net/LTG01/article/month/2015/12'

# req=requests.get(url)
#
# html = etree.HTML(req.text)
# result = html.xpath('//div/ul[@class="inf_list clearfix"]/li/a/text()')
#
# for i in result:
#     # if str(i).strip():
#     print(str(i).strip())
#     # print(i)

# result = html.xpath('//div/ul[@class="archive-list"]/li/a/text()')
# result2 = html.xpath('//div[@id="asideArchive"]/div/ul[@class="archive-list"]/li/a/span/text()')
# print(len(result),result)
# print(len(result2),result2)
# result3=[]
# for i in  result:
#     if str(i).strip():
#         result3.append(str(i).strip())
#
# print(len(result3),result3)
#
# for i in  zip(result3,result2):
#     # if str(i).strip():
#     print(str(i[0]).strip(),str(i[1]).strip())
#     # print(i)

#
# re = html.xpath('//div[@class="article-list"]/div[starts-with(@class,"article-item-box")]')
#
# for i in re:
#     nameType=i.xpath('.//a/span/text()')
#     name = i.xpath('.//a/text()')
#     span = i.xpath('.//span/text()|.//a/text()')
#     # print(len(name), name)
#     # print(len(span),span)
#     print(span[1])
    # for n in span:
    #     if str(n).strip():
    #         print(span.index(n),str(n).strip())
    # print(nameType,name)
    # print(i,type(i))


# 获取第一个
# result = html.xpath('//li[1]/a/text()')
# print(result)
# # 获取最后一个
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# # 获取前两个
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# # 获取倒数第三个
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)


# string="<Selector xpath='.//span/text()|.//a/text()' data='原创'>"
#
# print(string[string.find("data='")+6:-2])
import json
import pprint
import os


def downLoad(songIds,index):
    url='http://play.taihe.com/data/music/songlink'
    data='songIds={}&hq=0&type=m4a%2Cmp3&rate=&pt=0&flag=-1&s2p=-1&prerate=-1&bwt=-1&dur=-1&bat=-1&bp=-1&pos=-1&auto=-1'.format(songIds)
    req=requests.post(url,data=data)
    res=req.json()
    artistName='无名'
    try:
        songLink=res['data']['songList'][0]['songLink']
        songName=res['data']['songList'][0]['songName']
        artistName=res['data']['songList'][0]['artistName'].split(',')[0]
    except Exception as e:
        pprint.pprint(res)
        print(artistName,str(e))
        return
    if not artistName:
        artistName='无名'
    songId=res['data']['songList'][0]['songId']
    # print(songName,artistName,songId,songLink)
    if not os.path.exists('./'+artistName):
        os.makedirs('./'+artistName)
    re=requests.get(songLink)
    with open(artistName+'/'+songName+'.mp3','wb') as f:
         f.write(re.content)
    print('完成第'+str(index)+'首下载',songName,artistName,songId)


def getsongOnePageIds(start=0,size=15,artistID=2517):
    # url='http://music.taihe.com/artist/2517'
    # req=requests.get(url)
    # html = etree.HTML(req.text)
    # result = html.xpath('//span/a[starts-with(@href,"/song/")]/@href')
    # return result
    url='http://music.taihe.com/data/user/getsongs?start={0}&size={1}&ting_uid={2}'.format(start,size,artistID)
    req = requests.get(url)
    res=re.findall(r'<a href=\\"\\/song\\/(.*?)\\"',req.text)
    print(len(res),res)
    return res




def getAllPages(artistID=2517):
    url='http://music.taihe.com/artist/'+str(artistID)
    req = requests.get(url)
    # pprint.pprint(req.text)
    html = etree.HTML(req.text)
    pprint.pprint(html)
    # res = html.xpath('.//div[starts-with(@class,"list-box song-list-box")]/div[starts-with(@class,"page_navigator-box")]/div[starts-with(@class,"page-navigator-hook")]/div[starts-with(@class,"page-cont")]/div[starts-with(@class,"page-inner")]/a[starts-with(@class,"page-navigator-number")]/text()')
    # res = html.xpath('.//div[starts-with(@class,"list-box song-list-box")]/div/div/div/div/a[starts-with(@class,"page-navigator-number")]/text()')
    res = html.xpath('.//div[starts-with(@class,"list-box song-list-box")]/div/div[starts-with(@class,"page-navigator-hook")]/@class')
    print(len(res), res)
    total=re.findall(" 'total':(.*?),",res[0])[0]
    size = re.findall(" 'size':(.*?),", res[0])[0]
    print(int(total),int(size))
    return int(total),int(size)
def getArtistIDs():
    url='http://music.taihe.com/artist'
    req = requests.get(url)
    # pprint.pprint(req.text)
    html = etree.HTML(req.text)

    res = html.xpath('.//a[starts-with(@href,"/artist/")]/@href')
    # res = re.compile(r"//artist//[0-9]\+",req.text)

    print( res)
    return res


import re
if __name__ == '__main__':
    down=[]
    for artistID in getArtistIDs():
        artistID=artistID[artistID.rfind('/')+1:]
        try:
            int(artistID)

            if artistID in down:
                continue
            down.append(artistID)
        except Exception as e:
            continue
        # print(id)
        # # tt='/artist/2517'
        # index=tt.rfind('/')
        # print(tt[index+1:])
        #
        # re=getsongOnePageIds()
        # for i in re:
        #     downLoad(i[6:])
        # tt='/song/242078437'
        # print(tt[6:])
        # url = 'http://music.taihe.com/data/user/getsongs?start=0&size=15&ting_uid=2517'

        # artistID=2517
        total,size = getAllPages(artistID)
        pageSize = total/size
        if total%size != 0:
            pageSize += 1
        songids=[]
        for index in range(1,int(pageSize)+1):
            reids = getsongOnePageIds((index-1)*size,size,artistID)
            songids.extend(reids)
        index=0
        for id in songids:
            index+=1
            downLoad(id,index)










