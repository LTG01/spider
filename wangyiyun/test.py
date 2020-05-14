from user_agent.user_agent import agent
import requests
from lxml import etree
from copyheaders import headers_raw_to_dict
import os
from selenium import webdriver
#
# headers={
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
# 'Referer': 'https://music.163.com/',
# # 'Cookie':'_iuqxldmzr_=32; _ntes_nnid=5cee440c001730ce7f9f5723655f9503,1586670054202; _ntes_nuid=5cee440c001730ce7f9f5723655f9503; WM_TID=io4sMECelzJBQUVEFBNqEjjk%2FCvhT5Rw; WM_NI=1zdIoYMNy%2FaEBI932TsclHQTmlEI7UaEZDOwiHIu%2FPqN5ikR%2FdgjSP4PEUft4lqBtMeT2LjNep9ufVpXH9fM781CAY92OrJ5ur3%2BBdiK5vEJ1%2F1GMiFSdqzZcPO8H6UidWU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9f745869388a2f35382868eb2d44e828a9aabf44eb68df8a4e833a2ec88d4d92af0fea7c3b92af3a6acaaee538f92b7d0e44f8297f7d4b160b1bda4a9d460afb48baab65fa39b96a5ce7dab988796ae5cb392fb8aea5aedbca98bd25cf8908bb6e580f8b4bfa3f747a78cfeade946a7b0f796e55eb48888dae547f5e8ffa4c453fbee8193c93fb7aefdccc170ab95fb97c842f3f1ffa8d063868dac92f952a19081d9cb3e97b7acb8d837e2a3; playerid=99416119; JSESSIONID-WYYY=c4UPN3dyINougU%2BZF%2BVgI%5Cuc2tsnng6xRMbQcyCDNUO%5CAyPQnNn%2BOW4WEekvKMV7TTegGF3y6OZ9uXxxlSE7jxZGEZmUwN%5C%2F5Oq61sFAtrV%2F6NsJB7vReXnJDrEYCKY%5Chn4a%2F341dlGKs8A7%2FVzjSGrHp2Uo1y5FN7EpsZis0Hiwzj%2Bp%3A1588307408305',
# }
#
# headers='''
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh-CN,zh;q=0.9
# Connection: keep-alive
# Cookie: _iuqxldmzr_=32; _ntes_nnid=5cee440c001730ce7f9f5723655f9503,1586670054202; _ntes_nuid=5cee440c001730ce7f9f5723655f9503; WM_TID=io4sMECelzJBQUVEFBNqEjjk%2FCvhT5Rw; WM_NI=1zdIoYMNy%2FaEBI932TsclHQTmlEI7UaEZDOwiHIu%2FPqN5ikR%2FdgjSP4PEUft4lqBtMeT2LjNep9ufVpXH9fM781CAY92OrJ5ur3%2BBdiK5vEJ1%2F1GMiFSdqzZcPO8H6UidWU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9f745869388a2f35382868eb2d44e828a9aabf44eb68df8a4e833a2ec88d4d92af0fea7c3b92af3a6acaaee538f92b7d0e44f8297f7d4b160b1bda4a9d460afb48baab65fa39b96a5ce7dab988796ae5cb392fb8aea5aedbca98bd25cf8908bb6e580f8b4bfa3f747a78cfeade946a7b0f796e55eb48888dae547f5e8ffa4c453fbee8193c93fb7aefdccc170ab95fb97c842f3f1ffa8d063868dac92f952a19081d9cb3e97b7acb8d837e2a3; playerid=99416119; JSESSIONID-WYYY=NstKVHYav%2FhDJHacc2QwzNuPtRPHymk9hIh%2B0jW4JDEEItflUC%2B%2FpMOJi8C5gqMlWhOX5Mfa%2FCiGMmrRbK%2BEdDb09yxO5krg3DlUeo7FvD2bIQfut2wyv%2BKPaXszQeTmchqwFy18sPIxgJD4Iru1SXkIkR%2B7glRqOEzlt%2Bd%2BHDPZbGgU%3A1588312630394
# Host: music.163.com
# Referer: https://music.163.com/
# Sec-Fetch-Dest: iframe
# Sec-Fetch-Mode: navigate
# Sec-Fetch-Site: same-origin
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'''
# h = bytes(headers, encoding="utf-8")
# headers = headers_raw_to_dict(h)



headers = '''
authority: music.163.com
method: GET
path: /
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6
cache-control: max-age=0
cookie: _iuqxldmzr_=32; _ntes_nnid=df5a2087ca2abb70b4bd3d6170b71dd8,1576462996114; _ntes_nuid=df5a2087ca2abb70b4bd3d6170b71dd8; WM_TID=FAq2Izmu0OhBQVVRVEdtrgGglTVpU2XD; WM_NI=Ixn8HGuhi6m6UnVf3aZbSOHiXTaPPkbaWn0cillgVZAecQsakDyUwcw%2B2U1SU2FcAMPShnFqcQcZ247MWWbO96%2B4DOE37wV%2BhJnSdG7mHVrvW4dQZSkLaSdnzu%2Blo8umOWg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d85fa59996d8b56682928eb3c85e929b9abbb825b1a9ad83b2538cedbdadf92af0fea7c3b92a8ba8a2d9cb4db7b8a7d7f03e97b29a87b26b9abe9db0cb639c8cafb1d361a2bf998fb369abb4a488d55283bbadb2f26ba99cb7b6f669b5f5feb6b45997ee8a84c447948da88fc57ba18fadbbb140f59399b8e145fbeae5d5c74587edf998d521ac96a2b4e74df5b388b7f17e95ecacb2d959a994afb4e766baabe58dee34b7b381b8e637e2a3; JSESSIONID-WYYY=Dtz2qrqubvoAeyIW1F1NCF7uF2yk3wSP%2B8Qo3jyBoIk6%2BPjP2JYn970Cc2Sf1%2Bp3%5CfFEvaoueYJmHAtnQobcm8k4hWagBqBQ4ThVZQwdennHsWMke%2Fk6vU28EqQk5uvjUvaAPCcg%2Bi7n3N4CI33dtB7cNKJ%2FkbhW9uCneafzS6i7qOfd%3A1579005850713
referer: https://music.163.com/
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'''
h = bytes(headers, encoding="utf-8")
headers = headers_raw_to_dict(h)

# url='https://music.163.com/#/artist/album?id=12138269'

url = 'https://music.163.com/artist/album?id=12138269'
url='https://music.163.com/#/artist/album?id=12138269&limit=12&offset=12'
# URL='https://music.163.com/playlist?id=2008272804'
#
# url='https://music.163.com/playlist?id=2008272804'

# url = 'https://music.163.com/playlist?id=4876701785'

datas = requests.get(url, headers=headers)
sku_html = etree.HTML(datas.text)
print(datas.text)

# plist=sku_html.xpath('//*[@id="m-song-module"]/li/p[1]')
# print(plist)
# ttlist=[]

# for i in sku_html.xpath('//*[@id="m-song-module"]/li/p[1]'):
#     id = i.xpath('./a/@href')
#     name = i.xpath('./a/text()')
#
t=[(i.xpath('./a/text()')[0],i.xpath('./a/@href')[0]) for i in sku_html.xpath('//*[@id="m-song-module"]/li/p[1]')]
import time
import random
for i in t:
    time.sleep(random.randint(1,5))
    print(i)
    path=i[0]
    os.makedirs(path,exist_ok=True)
    url = 'https://music.163.com{}'.format(i[1])
    print(url)
    res= requests.get(url,headers=headers).text
    print(res)
    sku_html = etree.HTML(res)
    # kk=sku_html.xpath("//ul[@class='f-hide']/li")
    #
    # for i in kk:
    #     id = i.xpath('./a/@href')
    #     name = i.xpath('./a/text()')

    tt = [(i.xpath('./a/text()')[0], i.xpath('./a/@href')[0].split('=')[1]) for i in
         sku_html.xpath("//ul[@class='f-hide']/li")]

    print(tt)
    for song in tt:
        songUrl = 'https://link.hhtjim.com/163/{}.mp3'.format(song[1])  # 网易音乐
        print(songUrl)
        time.sleep(0.6)
        response = requests.get(songUrl)
        res = response.content
        pathname= path+'/'+song[0]

        with open(pathname+'.mp3', 'wb') as f:
            f.write(res)



# driver = webdriver.Chrome()
#
# driver.get(url)
#
# print(driver.page_source)