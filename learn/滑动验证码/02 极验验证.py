import random
import re
import time
from io import BytesIO

import requests
from PIL import Image
from selenium import webdriver

# 创建一个浏览器对象
driver = webdriver.Chrome()
# 打开登录页面
driver.get('http://www.cnbaowen.net/api/geetest/')
driver.maximize_window()
driver.implicitly_wait(10)
"""滑动验证"""
hover = driver.find_element_by_css_selector('.gt_slider_knob')

"""下载图片"""


def get_distance(image1, image2):
    """
    拿到滑动验证码需要移动的距离
    :param image1:没有缺口的图片对象
    :param image2:带缺口的图片对象
    :return:需要移动的距离
    """
    # print('size', image1.size)
    # rgb的差值不超过这一个范围 误差范围
    threshold = 50
    for i in range(0, image1.size[0]):  # 260
        for j in range(0, image1.size[1]):  # 160
            pixel1 = image1.getpixel((i, j))
            pixel2 = image2.getpixel((i, j))
            res_R = abs(pixel1[0] - pixel2[0])  # 计算RGB差
            res_G = abs(pixel1[1] - pixel2[1])  # 计算RGB差
            res_B = abs(pixel1[2] - pixel2[2])  # 计算RGB差
            if res_R > threshold and res_G > threshold and res_B > threshold:
                return i  # 需要移动的距离


def get_image(driver, div_path):
    """
    下载无序的图片  然后进行拼接 获得完整的图片
    :param driver: 浏览器对象
    :param div_path: 根据路径提取图片
    :return:
    """
    time.sleep(2)
    # 获取图片地址
    background_images = driver.find_elements_by_xpath(div_path)
    # 图片位置信息
    location_list = []
    # 获取图片碎片
    for background_image in background_images:
        # 当前碎片位置
        location = {}
        # 匹配当前图片碎片的地址，位置
        result = re.findall('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;',
                            background_image.get_attribute('style'))
        # print(result)
        location['x'] = int(result[0][1])
        location['y'] = int(result[0][2])

        image_url = result[0][0]
        # 将当前碎片信息添加到图片位置信息列表
        location_list.append(location)

    print('==================================')
    # 获取图片,
    image_url = image_url.replace('webp', 'jpg')
    # '替换url http://static.geetest.com/pictures/gt/579066de6/579066de6.webp'
    image_result = requests.get(image_url).content
    # 保存图片数据
    # with open('1.jpg','wb') as f:
    #     f.write(image_result)
    # 是一张无序的图片
    image_file = BytesIO(image_result)
    # image = merge_image(image_file, location_list)
    return image_file, location_list


def merge_image(image_file, location_list):
    """
     拼接图片
    :param image_file:
    :param location_list:
    :return:
    """
    # 乱序的图片
    im = Image.open(image_file)
    # im.show()
    new_im = Image.new('RGB', (260, 116))
    # 把无序的图片 切成52张小图片
    im_list_upper = []
    im_list_down = []
    # print(location_list)
    # 把所有的碎片位置遍历出来
    for location in location_list:
        # print(location['y'])
        if location['y'] == -58:  # 上半边
            # 如果是上半部分的,就切上半部分的
            # crop 裁剪图片 x, y
            print(location['x'])
            im_list_upper.append(im.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
        if location['y'] == 0:  # 下半边
            # 如果位置是下半部分的,就切割下半部分的
            im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

    # 还原上半部分
    x_offset = 0
    for im in im_list_upper:
        new_im.paste(im, (x_offset, 0))  # 把小图片放到 新的空白图片上
        x_offset += im.size[0]
    # 还原下半部分
    x_offset = 0
    for im in im_list_down:
        new_im.paste(im, (x_offset, 58))
        x_offset += im.size[0]
    # new_im.save('1.png')
    # new_im.show()
    return new_im


def get_track(distance):
    """
    拿到移动轨迹，模仿人的滑动行为，先匀加速后匀减速
    匀变速运动基本公式：
    ① v=v0+at
    ② s=v0t+(1/2)at²
    ③ v²-v0²=2as

    :param distance: 需要移动的距离
    :return: 存放每0.2秒移动的距离
    """
    print("distance", distance)
    # 初速度
    v = 0
    # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
    t = 2
    # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
    tracks = []
    # 当前的位移
    current = 0
    # 到达 mid 值开始减速(中点)
    mid = distance * 7 / 8
    # 多划出去 10 像素
    distance += 10  # 先滑过一点，最后再反着滑动回来
    # a = random.randint(1,3)
    while current < distance:
        # 设置速度
        if current < mid:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            a = random.randint(2, 4)  # 加速运动
        else:
            a = -random.randint(3, 5)  # 减速运动

        # 初速度
        v0 = v
        # 0.2 秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表
        tracks.append(round(s))

        # 速度已经达到v,该速度作为下次的初速度
        v = v0 + a * t

    print(tracks)
    total = sum(tracks)
    # 对超出的移动的内容进行修正
    while (total - distance) > -13:
        # 反着滑动到大概准确位置
        tracks.append(-random.randint(2, 3))
        total = sum(tracks)

    print('tracks', tracks)
    print('sumtracks', sum(tracks))
    return tracks


driver.implicitly_wait(10)

"""整个滑动的长度"""
# 1. 获取图片
# selenium 是自动化测试工具
# 1. 获取图片, 获取图片碎片的位置
image1_file, image1_location = get_image(driver, '//div[@class="gt_cut_fullbg gt_show"]/div')
image2_file, image2_location = get_image(driver, '//div[@class="gt_cut_bg gt_show"]/div')
print(image1_file, image1_location)
print(image2_file, image2_location)
# 2. 还原图片数据
image1 = merge_image(image1_file, image1_location)
image2 = merge_image(image2_file, image2_location)
# 3. 求出需要移动的距离
distance = get_distance(image1, image2)
print(distance)
# 4. 构建移动轨迹
tracks = get_track(distance)
print(tracks)
"""滑动动作链"""
# 使用动作链进行滑动验证
action = webdriver.ActionChains(driver)
# 点击, 并且不释放
action.click_and_hold(hover).perform()

for track in tracks:
    # 操作本身就会有延时
    # 只要动作不像机器就没事
    action.move_by_offset(track, 0)
# 释放
action.release().perform()

"""
多敲多练, 理解代码
"""