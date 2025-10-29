import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv


#1. page installing
url = "https://cbr.ru/currency_base/daily/"
responce = requests.get(url)
# print(dir(responce))
# print(responce.text)

#soup = BeautifulSoup(responce.text, 'html.parser')

soup = BeautifulSoup(responce.text, 'html.parser')

table = soup.find('table', class_='data')

#извлечение строк таблицы
rows = table.find_all('tr')[1:]

#подготовка файла csv
filename = f"currency_rates"

with open(filename, mode='w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['№','Цифровой код','Буквенный код','Единиц','Валюта','Курс'])
    dict = {}
    for row in rows:
        cols = []

        for col in row.find_all('td'):
            cols.append(col.text.strip())
        writer.writerow(cols)
        # print(cols)
        curr = cols[1]
        value = float(cols[4].replace(",","."))/int(cols[2])
        # value = cols[4]
        dict1 ={curr:value}
        dict.update(dict1)
    dict.update({'RUB':1.0})
    #print(dict)


st.title("Конвертер валют")
x = st.number_input("Сумма", min_value=0.0, value=1.0, step=1.0)
input = st.selectbox("Из", list(dict.keys()))
output = st.selectbox("В", list(dict.keys()))

if input == output:
    st.success(str(x) + ' ' + output)
else:
    st.success(str(round(x*dict.get(input)/dict.get(output),2)) + ' ' + output)