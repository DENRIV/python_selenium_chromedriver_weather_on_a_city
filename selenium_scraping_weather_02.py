
# python selenium_scraping_weather_02.py

# Libs.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

import time
import pandas as pd

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# chromedriver
driver = webdriver.Chrome(executable_path=r"D:\SW\chromedriver90\chromedriver.exe",chrome_options=options)

# max.
driver.maximize_window()

# Start Screen
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)
# time.sleep(3600) # let the browser die after 1 hour

url = 'https://www.eltiempo.es/madrid.html?v=por_hora'

# Start browser
driver.get(url)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.'))))\
    .click()
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')))

texto_columnas = driver.find_element_by_xpath('/html/body/div[7]/main/div[4]/div/section[4]/section/div[1]/ul')
texto_columnas = texto_columnas.text

tiempo_t = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

print(tiempo_t)

tiempo_t = [item for item in tiempo_t if item != "0.1" ]

print(tiempo_t)

horas = list()
temp = list()
v_viento = list()

for i in range(0, len(tiempo_t), 4):
    horas.append(tiempo_t[i])
    temp.append(tiempo_t[i+1])
    v_viento.append(tiempo_t[i+2])

df = pd.DataFrame({'Hours': horas, 'Temperature': temp, 'V_wind_Km_h':v_viento})

df['Temperature'] = df['Temperature'].str.replace('°','')
df['V_wind_Km_h'] = df['V_wind_Km_h'].str.replace('°','')

print(df)
df.to_csv('weather_today.csv', index=False)

driver.quit()
