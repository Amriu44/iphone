import requests
from bs4 import BeautifulSoup
from GettingData import product_links


# Collecting detaile and information about each iPhone product from the links collected in GettingData.py
data = []
for link in product_links:
    link_get = requests.get(link)
    soup = BeautifulSoup(link_get.text, 'html.parser')
    titels = soup.find_all('div' , attrs={"class":"kt-base-row__start kt-unexpandable-row__title-box"})
    values = soup.find_all('div' , attrs={"class":"kt-base-row__end kt-unexpandable-row__value-box"})
    temp = {}
    for y, z in zip(titels, values):
        temp[y.text] = z.text
    data.append(temp)

