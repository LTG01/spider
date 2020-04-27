
import requests
headers={
    # 'referer': 'https://www.kugou.com/song/15qg58b7.html',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.3'
}

# songUrl='http://music.163.com/song/media/outer/url?id={}.mp3'.format('1413585838')

songUrl='https://link.hhtjim.com/163/450853439.mp3' #网易音乐

songUrl='https://link.hhtjim.com/163/10919962.mp4'

# songUrl = 'https://link.hhtjim.com/qq/000OjsEW0QrPAd.mp3' #qq音乐
# response = requests.get(songUrl)

# response = requests.get(songUrl,headers=headers)
# res = response.content
#
# with open('wy_mv.mp4', 'wb') as f:
#     f.write(res)

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# url='https://music.163.com/#/discover/toplist'
#
#
#
# chrome_options = webdriver.ChromeOptions()
# # 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')  # //增加无界面选项
# chrome_options.add_argument('--disable-gpu')  # //如果不加这个选项，有时定位会出现问题
#
# # 启动浏览器，获取网页源代码
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# browser.get(url)
#
# response = browser.page_source
#
# print(response)

url='https://music.163.com/weapi/song/enhance/player/url/v1'

data={
'params': '0fV+NPVGBtpGxgrXv3xylsTJAFgJSdi0EZctlc5NacQ0wG1iGpedoTG6posU8+bUQm2E5cm5eJ9lsM5uoQttAg/U3p3fXHhJEReBc0k8lfAdSmzD/yvHNyhVs6igEWGJpM6XD7jcQaLqC+JekkVxMQ==',
   'encSecKey':'139d817995b129411bf1fd48ad83a26faba3ee92c23e3946580cd3f598433e97bc56c97ef5d99bcf6bc13daf116456395277571be9d9c8b7fd7693f29f04fede9431bfb039c636043c9b9f611a175ad35b3bca5c2f39c471c8f8ef94929f7f48b72c1668a788656c13b39d72507c632278ffee014a7bdf36e13578a4f5da10fb'
}


data2={'params': "YSijMnmkXHGMen3j5zlha/BYQUT2+vM7wPckApIEkxJ2l4vBog…Swq4zmF0nypX1A6xGjmHU9MkDAjeuIzZuhKu2IB7sZm6FAw==",
      'encSecKey': "59d1ef891cdbda55f90706ed747739e23d955bdb7eb2474671…817077d12f1ec13f2f765126855b694e6d18726791db22fb4"}


data={'params': "QM1ByMoO+1HtEdzuH9OzSbnvzn1XtClCBnb7Gp6iUqVgyg7epww6vvL9oEC7FbmJIstOcOG8b9Z7E5lFeRs9RC5M6og0TXEhzjP/qa+sOksvjOIfSWeNLwrRBv5XTkpOKsvNIcGEOMQGF6CWMj8Qhg==",
      'encSecKey': "b97a0ce755ba3ee69d5796e201e561fe59f9e48f1374a8f5ce1fd606ba173465619013f4193e18b2f84e33d1be5d4a59c2b1a848ea72c0374bef592796f017a6572743333639104b335360c93555c6fecba089ad4ddc3fe44d798e131e6f8f717c37e8acd11b4d8f129ec0c93d61e6564fba3950a4f2246066421e23c91d8be0"}



headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',

}

res = requests.post(url,data=data,headers=headers).json()
print(res)

uu=res['data'][0]['url']
id=res['data'][0]['id']
print(uu)

res = requests.get(uu).content

with open(str(id)+'.mp3','wb') as f:
    f.write(res)