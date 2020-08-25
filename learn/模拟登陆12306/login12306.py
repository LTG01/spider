import time
from PIL import Image

from selenium import webdriver
from selenium.webdriver import ActionChains
from chaojiying_Python.chaojiying import *

#登陆界面url
url = 'https://kyfw.12306.cn/otn/login/init'


#实例对象
drive = webdriver.Chrome()
# drive.maximize_window()
drive.get(url)

time.sleep(2)
drive.maximize_window()
time.sleep(2)
#截图登陆界面，保存为12306.png
drive.save_screenshot('12306.png')
time.sleep(2)
#定位验证码图片位置
img_code=drive.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')

#获取验证码图片 起点坐标
location = img_code.location
print(location)
#获取验证码图片长和宽
size = img_code.size
print(size)

#验证码图片在整个截图中占据的位置
# rangle=(int(location['x'])+320,int(location['y'])+270,int(location['x']+size['width'])*2,int(location['y']+size['height'])*2)
rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
# rangle=(int(location['x'])*2,int(location['y'])*2,int(location['x']+size['width'])*2,int(location['y']+size['height'])*2)
code_img_name='code.png'

img = Image.open('./12306.png')

print(rangle)
frame = img.crop(rangle)
frame.save(code_img_name)

chaojiying = Chaojiying_Client('yiqieanran01', '1qazxsw23edc', '904611')  # 用户中心>>软件ID 生成一个替换 96001


im = open(r'C:\LTG\code\spider\learn\模拟登陆12306\code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//

code=chaojiying.PostPic(im, 9004)['pic_str']
print(code)
#227,230|318,185

#处理返回的坐标
pointlist=[]
if '|' in code :
    pointlistStr=code.split('|')
    pointlist=[(int(pointStr.split(',')[0]),int(pointStr.split(',')[1])) for pointStr in pointlistStr ]
else:
    pointlist=[(int(code.split(',')[0]),int(code.split(',')[1]))]

for point in pointlist:

    ActionChains(drive).move_to_element_with_offset(img_code,point[0],point[1]).click().perform()
    time.sleep(0.5)
drive.find_element_by_id('username').send_keys('17628040175')
time.sleep(2)
drive.find_element_by_id('password').send_keys('2014LTG')
time.sleep(2)
drive.find_element_by_id('loginSub').click()
time.sleep(10)



time.sleep(3)
drive.quit()







