from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'

browser = Firefox()

browser.get(url)

#p = browser.find_element(By.TAG_NAME, "p")
sleep(3)

p = browser.find_element(By.TAG_NAME, 'p')
a = browser.find_element(By.TAG_NAME, 'a')

for click in range(1, 10):
    a.click()
    p.text==click
