import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


import pandas as pd
import re
from bs4 import BeautifulSoup
from requests import get
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import re
import io
import bs4
import wsurlopen
sns.set()


barrios=[]
prices=[]
areas=[]
rooms=[]
baths=[]
garages=[]
descriptions=[]
otros=[]
urls=[]
items=[]

i=0

with io.open("scrapingfr2.csv","w", encoding="utf8") as f1:
    f1.write("url; cod; barrio; price; area; room; bath; garage; boxcube; description\n")
a=0
for i in range(0,60):
    i=i+1
    url="https://www.fincaraiz.com.co/apartamento-casa-finca-casa-campestre-casa-lote-apartaestudio/venta/rionegro/?ad=30"
    url=url+"|"+str(i)+"|"+"|||1||8,9,7,21,23,22|||55|5500004||||||||||||||||1|||1||griddate%20desc||||-1||"
    urls.append(url)
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url)
    #links = driver.find_element_by_css_selector('#divAdverts ul:nth-child(n+5) li.title-grid a').get_attribute('href')
    links = driver.find_elements_by_css_selector('#divAdverts ul li.title-grid a')
    for link in links:
        item=link.get_attribute('href')
        items.append(item)
    driver.quit()
    print(len(items))
a=len(items)
print(a)

headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

for ite in items:
    # r = get(item, headers=headers)
    # page_html = BeautifulSoup(r.text, 'html.parser')
    # casas = page_html.find_all('div', class_="detail")
    var1=wsurlopen.urlopen(ite)
    readfull=bs4.BeautifulSoup(var1.text,'lxml')
    read1=readfull.select(".detail")
    #print(read1)
    for casa in read1:
        cod=casa.select(".description")
        cod=cod[1].getText()
        cod=(re.sub("Descripción Código Fincaraiz.com.co: ","", cod)).strip()
        cod = re.sub(r"\s+"," ", cod)
        #print(cod)

        barrio=casa.select(".box")
        barrio=barrio[0].getText()
        barrio = re.sub(r"\s+"," ", barrio)
        #print(barrio)

        price=casa.select(".price")
        price=price[0].getText()
        price = re.sub(r"\s+"," ", price)
        #print(price)

        area=casa.select(".advertSurface")
        area=area[0].getText()
        area=(re.sub(" m²","", area)).strip()
        area = re.sub(r"\s+"," ", area)
        #print(area)

        room=casa.select(".advertRooms")
        room=room[0].getText()
        room=(re.sub(" Habitaciones: ","", room)).strip()
        room = re.sub(r"\s+"," ", room)
        #print(room)

        bath=casa.select(".advertBaths")
        bath=bath[0].getText()
        bath=(re.sub("Baños: ","", bath)).strip()
        bath = re.sub(r"\s+"," ", bath)
        #print(bath)

        garage=casa.select(".advertGarages")
        garage=garage[0].getText()
        garage=(re.sub("Parqueaderos: ","", garage)).strip()
        garage = re.sub(r"\s+"," ", garage)
        #print(garage)

        boxcube=casa.select(".boxcube")
        boxcube=boxcube[3].getText()
        boxcube = re.sub(r"\s+"," ", boxcube)
        #print(boxcube)

        description=casa.select(".description")
        description=description[0].getText()
        description = re.sub(r"\s+"," ", description)
        #print(description)

        data= ite+";"+cod+";"+barrio+";"+price+";"+area+";"+room+";"+bath+";"+garage+";"+boxcube+";"+description+"\n"
        #print(data)
        with io.open("scrapingfr2.csv", "a", encoding="utf8") as f1:
            f1.write(data)
            f1.close()
print(a)







#



#         areas.append(area)
# #     room=container.find_element_by_class_name('advertRooms').text
# #     rooms.append(room)
# #     bath=container.find_element_by_class_name('advertBaths').text
# #     baths.append(bath)
# #     garage=container.find_element_by_class_name('advertGarages').text
# #     garages.append(garage)
# #     description=container.find_element_by_class_name('description').text
# #     #print(description)
# #     descriptions.append(description)
# #     otro = container.find_element_by_class_name('InitialUL').text
# #     print(otro)
# #     otros.append(otros)
# # driver.back()

# data = {'barrios': barrios, 'Precios': prices, 'areas': areas, 'rooms': rooms,'baths': baths, 'garages': garages, 'descripción':descriptions, 'otros':otros}
# datas=pd.DataFrame(data)
# print(datas.head())

