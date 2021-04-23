
# python selenium_scraping_weather_01.py

# Libs.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time
# import pandas as pd


#options = webdriver.ChromeOptions() 
#options.add_argument("start-maximized")
#driver = webdriver.Chrome(options=options)


options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(chrome_options=options)
# Open Browser about:blank ${BROWSER} options=add_experimental_option(‘excludeSwitches’, [‘enable-logging’])

# chromedriver
# driver = webdriver.Chrome(executable_path=r"D:\SW\chromedriver90\chromedriver.exe")
driver = webdriver.Chrome(executable_path=r"D:\SW\chromedriver90\chromedriver.exe",chrome_options=options)

# max.
driver.maximize_window()

# Start Screen
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
# time.sleep(3600) # let the browser die after 1 hour

url = 'https://eltiempo.es'

# Start browser
driver.get(url)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#inputSearch')))\
    .send_keys('Madrid')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon.icon-search')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'i.icon_weather_s.icon.icon-local')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[1]/a')))\
    .click()

# Full XPATH

# tab.1
#  /html/body/div[7]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[1]/a

# tab.2
#  /html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/section/ul/li[2]/a
#  /html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/section/ul/li[2]/a

# https://www.eltiempo.es/madrid.html?v=por_hora    

# tab.3
#  /html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[3]/a

# tab.4
# /html/body/div[7]/main/div[4]/div/section[4]/div[2]/section/ul/li[4]/a

driver.quit()
