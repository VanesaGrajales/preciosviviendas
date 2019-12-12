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
import verificacion
import lxml
sns.set()

items=[]
urls=[]
i=0

with io.open("scraping_fincas_ml.csv","w", encoding="utf8") as f1:
    f1.write("url; tipo_vivienda; barrio; price; area; room; bath; sup_total; area_const; antiguedad; piso; ambientes; adicionales; description\n")
a=49
url='https://listado.mercadolibre.com.co/inmuebles/fincas/venta/antioquia/rionegro/'
urls.append(url)
for i in range(49, 155, 48):
    url='https://listado.mercadolibre.com.co/inmuebles/fincas/venta/antioquia/rionegro/'
    url=url+"_Desde_"+str(i)
    #print(url)
    urls.append(url)
for url in urls:
    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url)
    links = driver.find_elements_by_css_selector('#searchResults li.results-item.highlighted.article.grid  a')
    for link in links:
        item=link.get_attribute('href')
        #print(item)
        items.append(item)
    driver.quit()
    #print(len(items))
a=len(items)
#print(a)
headers = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
for ite in items:
    var1=verificacion.abrir(ite)
    readfull=bs4.BeautifulSoup(var1.text,'lxml')
    read1=readfull.select(".layout-main.u-clearfix")
    #print(read1)
    for casa in read1:
        # cod=casa.select(".description")
        # cod=cod[1].getText()
        # cod=(re.sub("Descripción Código Fincaraiz.com.co: ","", cod)).strip()
        # cod = re.sub(r"\s+"," ", cod)
        # #print(cod)

        tipo_vivienda=casa.select(".vip-classified-info")
        tipo_vivienda=tipo_vivienda[0].getText()
        tipo_vivienda = re.sub(r"\s+"," ", tipo_vivienda)
        #print(tipo_vivienda)

        barrio=casa.select(".item-title__primary")
        barrio=barrio[0].getText()
        barrio = re.sub(r"\s+"," ", barrio)
        #print(barrio)

        price=casa.select(".price-tag-fraction")
        price=price[0].getText()
        #price = re.sub(r"\s+"," ", price)
        #print(price)

        try:

            area=casa.select(".align-surface")
            area=area[0].getText()
            area=(re.sub(" m² totales","", area)).strip()
            area = re.sub(r"\s+"," ", area)
            #print(area)
        except:
            area=""
            pass

        room=casa.select(".align-room")
        room=room[0].getText()
        room=(re.sub(" dormitorios","", room)).strip()
        room = re.sub(r"\s+"," ", room)
        #print(room)

        try:
            bath=casa.select(".align-bathroom")
            bath=bath[0].getText()
            bath=(re.sub(" baños","", bath)).strip()
            bath = re.sub(r"\s+"," ", bath)
            #print(bath)
        except:
            bath=""
            pass

        sup_total=casa.select(".specs-item")
        sup_total=sup_total[0].getText()
        sup_total=(re.sub("Superficie total","", sup_total)).strip()
        sup_total=(re.sub(" m²","", sup_total)).strip()
        sup_total = re.sub(r"\s+"," ", sup_total)
        #print(sup_total)

        try:
            area_const=casa.select(".specs-item")
            area_const=area_const[1].getText()
            area_const=(re.sub("Área construida","", area_const)).strip()
            area_const=(re.sub(" m²","", area_const)).strip()
            area_const = re.sub(r"\s+"," ", area_const)
        except:
            area_const=""
            pass
        #print(area_const)
        try:

            antiguedad=casa.select(".specs-item")
            antiguedad=antiguedad[4].getText()
            antiguedad=(re.sub("Antigüedad","", antiguedad)).strip()
            antiguedad=(re.sub(" años","", antiguedad)).strip()
            antiguedad = re.sub(r"\s+"," ", antiguedad)
        except:
            antiguedad=""
            pass
        #print(antiguedad)

        try:
            piso=casa.select(".specs-item")
            piso=piso[5].getText()
            piso=(re.sub("Antigüedad","", piso)).strip()
            piso=(re.sub(" años","", piso)).strip()
            piso = re.sub(r"\s+"," ", piso)
            #print(piso)
        except:
            piso=""
            pass

        try:
            ambientes=casa.select(".attribute-list")
            ambientes=ambientes[0].getText()
            ambientes=(re.sub("Parqueaderos: ","", ambientes)).strip()
            ambientes = re.sub(r"\s+"," ", ambientes)
            #print(ambientes)
        except:
            ambientes=""
            pass
        try:
            adicionales=casa.select(".attribute-list")
            adicionales=adicionales[1].getText()
            adicionales = re.sub(r"\s+"," ", adicionales)
            #print(adicionales)
        except:
            adicionales=""
            pass

        try:
            description=casa.select(".item-description__text")
            description=description[0].getText()
            description = re.sub(r"\s+"," ", description)
        except:
            description=""
            pass

        #print(description)

        data= str(ite)+";"+str(tipo_vivienda)+";"+str(barrio)+";"+str(price)+";"+str(area)+";"+str(room)+";"+str(bath)+";"+str(sup_total)+";"+str(area_const)+";"+str(antiguedad)+";"+str(piso)+";"+str(ambientes)+";"+str(adicionales)+";"+str(description)+"\n"
        print(data)
        print("hecho")
        with io.open("scraping_fincas_ml.csv", "a", encoding="utf8") as f1:
            f1.write(data)
            f1.close()
print(a)


