#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: isafuent
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime

# Iniciamos el driver de Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# URL inicial
driver.get('https://www.amazon.com.mx/s?k=iphone+15+amazon')

# Fecha de extracción
extractionDate = str(datetime.datetime.now().date())

# Lista donde almacenaremos los datos
products = []
nextBtn = True
e = 0

while nextBtn:
    time.sleep(3)
    # Encontramos todos los "items" de la página
    productos = driver.find_elements(By.XPATH, "//*[@role='listitem']")

    for producto in productos:
        try:
            # XPaths relativos para buscar dentro del elemento actual
            titulo = producto.find_element(By.XPATH, ".//*[@class='a-link-normal s-line-clamp-4 s-link-style a-text-normal']")
            precio = producto.find_element(By.XPATH, ".//*[@class='a-price-whole']")

            e += 1
            # Añadimos al listado únicamente: ID, Título, Precio y Fecha de extracción
            products.append((e, titulo.text, precio.text, extractionDate))

        except:
            # Si falla la búsqueda, continuamos con el siguiente
            continue

    # Intentamos pasar a la siguiente página
    next_page = driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[66]/div/div/span/ul/li[4]/span/a')
    if len(next_page) > 0:
        next_page[0].click()
    else:
        nextBtn = False

# Cerramos el navegador
driver.close()

# Imprimimos los resultados en una lista, con saltos de línea
# Formato deseado:
# 1.-
# Titulo
# Precio
# Fecha
# 
# 2.-
# ...

for p in products:
    print(f'{p[0]}.-')
    print(p[1])           # Nombre/Título
    print("$",p[2])           # Precio
    print(p[3])           # Fecha de extracción
    print()               # Línea en blanco para espaciar
