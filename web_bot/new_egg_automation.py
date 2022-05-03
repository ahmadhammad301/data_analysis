import os
from time import sleep
import login_pws #onother python file to store my login username
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys




os.environ['PATH'] = r"D:\selenium_driver"
driver = webdriver.Chrome()

driver.get('https://newegg.today/index/user/login.html')

usr = driver.find_element_by_xpath('//*[@id="login"]/form/div[1]/input')
pws = driver.find_element_by_xpath('//*[@id="login"]/form/div[2]/input')

usr.send_keys(login_pws.username)
pws.send_keys(login_pws.password)

login = driver.find_element_by_xpath('//*[@id="login"]/form/input[2]')
login.click()
driver.implicitly_wait(10)

try:
    ad_remove = driver.find_element_by_class_name('tanchuangClose')
    ad_remove.click()
    print('ad removed')
except:
    print("didn't find the ad")

#find shopee class and click on it 
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="index"]/div[2]/div[1]/div[7]/div[2]/div[1]/div[1]').click()

###################################################
# start gropping orders
# there was another element recieves the click therefore i managed to scroll down to make sure
# that the desired element where clicked
for _ in range(25):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="autoStart"]'))
        )
    get_order = driver.find_element(By.XPATH, '//*[@id="autoStart"]')
    get_order.location_once_scrolled_into_view
    get_order.click()
    
    sleep(20)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'confirm-btn'))
        )
    #wait 10 sec until page refreshed  
    driver.implicitly_wait(8)
    #click on submit order
    submit_order = driver.find_element(By.CLASS_NAME, 'confirm-btn')
    submit_order.click()
    sleep(50)
