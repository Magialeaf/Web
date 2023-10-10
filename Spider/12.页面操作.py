import random
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

op = Options()
# op.add_argument('--headless')
# op.add_argument('--disable-gpu')
op.add_experimental_option('excludeSwitches',['enable-automation'])

ser = Service(r"C:\Users\11323\Desktop\Update\chromedriver.exe")
driver = webdriver.Chrome(options=op,service=ser)

driver.get("https://www.taobao.com/")

tag = driver.find_element(by=By.XPATH,value="//*[@id='q']")
tag.send_keys("平板")

enter = driver.find_element(by=By.XPATH,value="//*[@id='J_TSearchForm']/div[1]/button")
ActionChains(driver).click(enter).perform()

for i in range(10):
    time.sleep(random.randrange(5,15) * 0.1)
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight / 10)")
driver.save_screenshot('1.png')


time.sleep(3)
driver.quit()
