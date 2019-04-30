import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "https://www.taobao.com"
#con = webdriver.ChromeOptions()
#con.add_argument('--headless')
browser = webdriver.Chrome()
browser.get(url)
print(browser.title)
browser.find_element_by_id('q').send_keys('iPad')
browser.find_element_by_css_selector('button').click()
print(browser.page_source)
