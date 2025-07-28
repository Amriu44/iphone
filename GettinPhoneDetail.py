import requests
from bs4 import BeautifulSoup
from GettingData import product_links
# product_links = {'https://divar.ir/v/iphone-11-pro-max-256-%D8%A7%DB%8C%D9%81%D9%88%D9%86-%DB%B1%DB%B1-%D9%BE%D8%B1%D9%88%D9%85%DA%A9%D8%B3-%DB%B2%DB%B5%DB%B6/AawMpiiK', 'https://divar.ir/v/12-pro-max/wZzSxUvR'}

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

