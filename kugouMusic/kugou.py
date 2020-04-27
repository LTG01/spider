import requests
import json
import re
import os
from lxml import etree
import random
import time
'''

爬取酷狗音乐榜单上的音乐，包含

1。热门榜单
    酷狗飙升榜
    酷狗top500
    网络红歌榜
    DJ 热歌榜
    酷狗雷达榜
    。。。


2。特色音乐棒
    电音热歌榜
    影视金曲榜
    。。。。

3。全球榜
    美国billboard 榜
    英国单曲榜
    。。。



'''

class kugou(object):

     def __init__(self,url,headers):
         self.url=url
         self.headers=headers

     def start(self):

         urlList ,typeNameList=self.getMusicTypeUrl()
         hashcodeList = self.getHashcode(urlList)


         self.getSongUrl(typeNameList,hashcodeList)


     def getMusicTypeUrl(self):
         '''
         根据 榜单页面的url，获取 每一个榜单的url 地址，以及对一个的榜单名称，便于后面分类存储
         :return:
         '''


         response=requests.get(self.url).text
         html = etree.HTML(response)

         musicTypeUrlList=html.xpath('/html/body/div[3]/div/div[1]/div[1]/ul/li/a[@href]/@href')
         musicTypeNameList = html.xpath('/html/body/div[3]/div/div[1]/div[1]/ul/li/a[@title]/@title')

         return musicTypeUrlList,musicTypeNameList



     def getHashcode(self,urlList):
         '''
         获取每一个榜单里面的 歌曲的hashcode，以及歌曲名称，每一个榜单页面的hashcode 和歌曲名称 分别存在一个列表 ，返回两个嵌套列表

         :param urlList: 存储每一个榜单类型的 URL 列表
         :param typeNameList: 存储每一个榜单对应的类型名称
         :return:
         '''


         # urlList ,typeNameList=self.getMusicTypeUrl()

         hashcodeList=[]
         fileNameList=[]
         for url in urlList:

            resp = requests.get(url).text

            hashcode = re.findall('"Hash":"(.*?)","', resp)

            print(len(hashcode), hashcode)
            hashcodeList.append(hashcode)

            fileName = re.findall('"FileName":"(.*?)","', resp)

            print(len(fileName), fileName)
            fileNameList.append(fileName)
            time.sleep(random.randint(1,5))

         return  hashcodeList

     def getSongUrl(self,typeNameList,hashcodeList):
         '''
         根据hsacode 获取每一首歌曲的路径

         :param typeNameList:
         :param hashcodeList:
         :return:
         '''

         all_files = [f for f in os.listdir()]  # 输出根path下的所有文件名到一个列表中
         # typeNameList,hashcodeList=self.getHashcode()

         for i in range(0,len(typeNameList)):

             typeName =typeNameList[i]

             hashcodelist=hashcodeList[i]
             if typeName in all_files :
                 continue

             print(typeName,len(hashcodelist))
             for h in hashcodelist:
                url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}'.format(h)
                time.sleep(random.randint(33, 60))



                resp=requests.get(url, headers=self.headers ).text
                data=json.loads(resp)
                print(data)
                try:
                    song_url=data['data']['play_url']
                    name=data['data']['song_name']
                    auName=data['data']['author_name']

                    path='./'+typeName

                    self.saveMusic(song_url,path,auName+"+"+name)
                except Exception as e:
                    print(str(e))

     def saveMusic(self, songUrl, path, name):
         time.sleep(random.randint(0, 36))
         if self.headers != {}:
             response = requests.get(songUrl, headers=self.headers).content
         else:
             response = requests.get(url).content

         os.makedirs(path, exist_ok=True)

         musicLocation = '{}/{}.mp3'.format(path, name)
         with open(musicLocation, 'wb') as f:
             f.write(response)


user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]

headers = {
    'user-Agent': random.choice(user_agent),
    'referer': 'https://www.kugou.com/song/',
'cookie': 'kg_mid=de37a1cfd40c173f2820dfe14f530c24; kg_dfid=33MGlt3ida3b0rgFCn3P1T2f; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1586955391,1587184891,1587196618,1587197865; kg_mid_temp=de37a1cfd40c173f2820dfe14f530c24; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1587210965',

}


url='https://www.kugou.com/yy/html/rank.html'



if __name__ == '__main__':

    kg=kugou(url,headers)
    kg.start()




















#
# import requests
# import  json
# import pprint
# from lxml import etree
# url='https://www.kugou.com/'
#
#
#
#
#
#
# # url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=46747EB410185C370ECC918021690871&mid=de37a1cfd40c173f2820dfe14f530c24'
#
#
# headers={
#     # 'referer': 'https://www.kugou.com/song/15qg58b7.html',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.3'
#
#
#
# }
# response = requests.get(url,headers=headers)
# res=response.text
# html = etree.HTML(res)
# rr=html.xpath('//*[@id="SongtabContent"]/ul[1]/li/@data')
#
# print(len(rr),rr)
#
# HashList=[]
# def getHash(rr):
#     for r in rr:
#
#         d= json.loads(r)
#
#         # print(type(rr))
#         # pprint.pprint(rr)
#
#         yield d['Hash'],d['FileName']
#
# for hash in getHash(rr):
#
#     url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}&mid=de37a1cfd40c173f2820dfe14f530c24'.format(hash[0])
#
#     response = requests.get(url, headers=headers)
#     res = response.text
#
#     rr= json.loads(res)
#
#     print(type(rr))
#     # pprint.pprint(rr)
#     world = rr['data']['lyrics']
#     lurl=rr['data']['play_url']
#     name = hash[1].split('-')[0].strip()
#     print(name)
#     response = requests.get(lurl, headers=headers)
#     res = response.content
#
#     with open(name+'.mp3','wb') as f:
#         f.write(res)
#
#
#
#
#
#
#
#
# #
# # from selenium import webdriver
# # import re
# # import time
# #
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # chrome_options = webdriver.ChromeOptions()
# # # 使用headless无界面浏览器模式
# # chrome_options.add_argument('--headless') #//增加无界面选项
# # chrome_options.add_argument('--disable-gpu') #//如果不加这个选项，有时定位会出现问题
# #
# # # 启动浏览器，获取网页源代码
# # browser = webdriver.Chrome(chrome_options=chrome_options)
# #
# # t=time.time()
# # # browser = webdriver.Chrome()
# # browser.get(url)
# #
# #
# # # ww=WebDriverWait(browser,10).until(EC.visibility_of(browser.find_element(by=By.ID,value='myAudio')))
# # # '''判断元素是否可见，如果可见就返回这个元素'''
# # #
# # # print(ww)
# #
# # response = browser.page_source
# #
# #
# # # print(f"browser text = {response}")
# #
# # # print(type(response))
# #
# # tt = re.findall('<audio class="music" id="myAudio" src="(.*?\.mp3)"',response)
# #
# # print(time.time()-t)
# # print(tt)
# #
# # browser.quit()
# #
# #
