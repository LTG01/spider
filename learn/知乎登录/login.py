from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


#C:\Users\LTG\AppData\Local\Google\Chrome\Application>chrome.exe --remote-debugging-port=9222
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome(executable_path="E:/chromedriver/chromedriver_win32/chromedriver.exe")
import time

try:
    browser.maximize_window()  # 将窗口最大化防止定位错误
except:
    pass
# browser.get("https://www.zhihu.com/signin")
# logo_element = browser.find_element_by_class_name("SignFlowHeader")
# y_relative_coord = logo_element.location['y']
# 此处一定不要将浏览器放大 会造成高度获取失败！！！
# browser_navigation_panel_height = browser.execute_script('return window.outerHeight - window.innerHeight;')
# time.sleep(5)
# browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys(Keys.CONTROL + "a")
# browser.find_element_by_css_selector(".SignFlow-accountInput.Input-wrapper input").send_keys(
#     "17628040175")
#
# browser.find_element_by_css_selector(".SignFlow-password input").send_keys(Keys.CONTROL + "a")
# browser.find_element_by_css_selector(".SignFlow-password input").send_keys(
#     "2014@ltg")
# time.sleep(5)
# browser.find_element_by_css_selector(
#     ".Button.SignFlow-submitButton").click()
# time.sleep(15)
from mouse import move, click
browser.get("https://www.zhihu.com/")

print(browser.get_cookies())