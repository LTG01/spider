from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import random
import time
url='http://www.cnbaowen.net/api/geetest/'
url = 'https://account.cnblogs.com/signin'

class SliderVerif(object):

    def __init__(self, url):
        # 创建一个浏览器对象
        self.driver = webdriver.Chrome()
        # 打开登录页面
        self.driver.get(url=url)
        # driver.maximize_window()
        self.driver.implicitly_wait(10)
        """滑动验证"""


    def start(self):
        input_username = self.driver.find_element_by_id('mat-input-0')
        input_password = self.driver.find_element_by_id('mat-input-1')
        input_username.send_keys('928480709')
        input_password.send_keys('dfcver1112223334')
        submitBtn = self.driver.find_element_by_css_selector(
            'body > app-root > div > mat-sidenav-container > mat-sidenav-content > div > div > app-sign-in > app-content-container > mat-card > div > form > div > button > span')
        submitBtn.click()
        time.sleep(2)  # 等待验证码加载
        self.driver.implicitly_wait(10)
        none_img = self.get_img(self.driver, 1)

        elementobj = self.driver.find_element_by_css_selector('.geetest_canvas_fullbg.geetest_fade.geetest_absolute')
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, 'style',
                              'display: block; opacity: 1;')
        time.sleep(1)
        block_img = self.get_img(self.driver, 2)
        geetest_slider_button = self.driver.find_element_by_class_name('geetest_slider_button')

        distance = self.get_distans(block_img, none_img)
        print(distance)
        err,tracks_dic = self.get_tracks(distance)

        forword_tracks = tracks_dic['forward_tracks']
        back_tracks = tracks_dic['back_tracks']
        ActionChains(self.driver).click_and_hold(geetest_slider_button).perform()
        self.start_action(forword_tracks,back_tracks)


    def get_img(self,img_element,index=1):
        img_element = self.driver.find_element_by_xpath(
            '//div[@class="geetest_panel_next"]//canvas[@class="geetest_canvas_slice geetest_absolute"]')

        size = img_element.size
        location = img_element.location
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        # snap_obj = get_snap(driver, i)
        self.driver.save_screenshot('snap{}.png'.format(index))
        snap_obj = Image.open('snap{}.png'.format(index))
        print(left, top, right, bottom)
        img_obj = snap_obj.crop((left, top, right, bottom))
        img_obj.save('snap1{}.png'.format(index))
        return img_obj

    def start_action(self, forword_tracks, back_tracks):
        '''
        先前进在后退
        :param forword_tracks:
        :param back_tracks:
        :return:
        '''

        # forword_tracks = tracks_dic['forward_tracks']
        # back_tracks = tracks_dic['back_tracks']
        for forword_track in forword_tracks:
            ActionChains(self.driver).move_by_offset(xoffset=forword_track,yoffset=0).perform()
        time.sleep(0.2)
        for back_track in back_tracks:
            ActionChains(self.driver).move_by_offset(xoffset=back_track,yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.3)
        ActionChains(self.driver).release().perform()


    def get_tracks(self, distance, **kwargs):
       '''
       获取运动轨迹
       :param distance:
       :param kwargs:
       :return:
       '''

       if not isinstance(distance, int):
           return -1, {'msg': '运动距离不是整数'}
       # 多向前运动一定距离
       move_more = int(kwargs.get('move_more', 20))
       distance += move_more
       s = 0
       v0 = 0
       t = kwargs.get('t', 0.4)
       per = kwargs.get('t', 0.6)
       mid = distance * per
       forward_tracks = []
       while s < distance:
           if s < mid:
               a = 3
           else:
               a = 1
           v = v0
           tance = v * t + 1 / 2 * a * (t ** 2)
           tance = round(tance)
           s += tance
           v0 = v + a * t
           forward_tracks.append(tance)
       # 生成后退轨迹
       # back_tracks = []
       # while True:
       #     if len(back_tracks) == 0 or abs(abs(sum(back_tracks)) - move_more) >= 4:
       #         num = random.randint(1, 4)
       #     elif 3 <= abs(abs(sum(back_tracks)) - move_more):
       #         num = random.randint(1, 3)
       #     elif 2 <= abs(abs(sum(back_tracks)) - move_more):
       #         num = random.randint(1, 2)
       #     else:
       #         num = 1
       #
       #     back_tracks.append(-num)
       #     print(back_tracks)
       #     if len(back_tracks) >= 1 and sum(back_tracks) == -move_more:
       #         break
       back_tracks = [-1, -1, -1, -2, -2, -2, -3, -3, -2, -2, -1]  # 20
       return 0, {"forward_tracks": forward_tracks, 'back_tracks': back_tracks, 'msg': 'success'}

    def get_distans(self, img1, img2, **kwargs):
       '''
       获取移动距离
       :param img1:
       :param img2:
       :param kwargs:
       :return:
       '''
       # 除去滑块的宽度，大概50个像素左右
       start_x = kwargs.get('start', 60)
       threhold = kwargs.get('threhold', 100)  # 阈值
       for x in range(start_x, img1.size[0]):
           for y in range(img1.size[1]):
               rgb1 = img1.load()[x, y]
               rgb2 = img2.load()[x, y]
               res1 = abs(rgb1[0] - rgb2[0])
               res2 = abs(rgb1[1] - rgb2[1])
               res3 = abs(rgb1[2] - rgb2[2])
               if not (res1 < threhold and res2 < threhold and res3 < threhold):
                   return x - 8







if __name__ == '__main__':

   sv = SliderVerif(url=url)
   sv.start()

   pass
