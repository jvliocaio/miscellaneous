from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time 
import urllib

url = 'https://web.whatsapp.com/'

number = '5524981803014'
txt = 'E au seu merda absurdo'
encoded = urllib.parse.quote('txt')
link = f'web.whatsapp.com/send?phone={number}?text={txt}'

browser = Firefox()

browser.get(url)
while len(browser.find_element(By.ID, ('pane-side'))) < 1:
    time.sleep(1)



browser.get('link')
while len(browser.find_element(By.ID, ('pane-side'))) < 1:
    time.sleep(1)
# browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p').send_keys(Keys.ENTER)