from selenium import webdriver as wbdrivr
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



def yt(name):
    driver = wbdrivr.Chrome('./chromedriver')
    driver.get('https://www.youtube.com/results?search_query=song+{name}}')
    driver.find_element_by_xpath('//*[@id="thumbnail"][0]')
    print('working.....')


