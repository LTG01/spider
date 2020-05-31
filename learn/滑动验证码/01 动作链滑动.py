from selenium import webdriver

# 创建一个浏览器对象
driver = webdriver.Chrome()
# 打开登录页面
driver.get('https://member.zjtcn.com/common/login.html')
driver.maximize_window()
"""滑动验证"""
hover = driver.find_element_by_css_selector('.ui-slider-btn')
"""
.click
.send_keys
.clear
"""
# 使用动作链进行滑动验证
# 动作链绑定到对应的实例对象上去
action = webdriver.ActionChains(driver)
# 点击, 并且不释放
action.click_and_hold(hover).perform()
# 往x方向滑动 85 像素 340
# 滑动轨迹
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)
action.move_by_offset(85, 0)
# 释放
action.release().perform()
input()
