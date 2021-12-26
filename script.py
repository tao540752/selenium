import time

from selenium import webdriver
from selenium.webdriver import ActionChains

drive=webdriver.Chrome(r'C:\putao\chromedriver.exe')
drive.maximize_window()

def move_to_gap(self, slider, track):
    """
    拖动滑块到缺口处
    :param slider: 滑块
    :param track: 轨迹
    :return:
    """
    ActionChains(self.browser).click_and_hold(slider).perform()
    for x in track:
        ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(self.browser).release().perform()


def login(url):
    drive.implicitly_wait(3)
    drive.get(url=url)
    element=drive.find_element_by_xpath('//iframe[@style="height: 300px; width: 300px;"]')
    drive.switch_to.frame(element)
    drive.find_element_by_xpath('//*[@class="account-tab-account"]').click()
    drive.find_element_by_xpath('//*[@id="username"]').send_keys('18027290140')
    drive.find_element_by_xpath('//*[@id="password"]').send_keys('540752860')
    drive.find_element_by_xpath('//*[@class="btn btn-account btn-active"]').click()
    time.sleep(2)
    drive.switch_to.default_content()

login(r'https://www.douban.com/')
element=drive.find_elements_by_css_selector(".nav-user-account")
if len(element)>0:
    print('登录成功')
else:
    print('登录失败')
drive.quit()

