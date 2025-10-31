import streamlit as st
import requests
from bs4 import BeautifulSoup
import csv

from write_to_csv import write_rows_to_csv


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
filename = f"currency_rates.csv"

dict = write_rows_to_csv(filename, rows)


st.title("Конвертер валют")
x = st.number_input("Сумма", min_value=0.0, value=1.0, step=1.0)
input = st.selectbox("Из", list(dict.keys()))
output = st.selectbox("В", list(dict.keys()))

if input == output:
    st.success(str(x) + ' ' + output)
else:
    st.success(str(round(x*dict.get(input)/dict.get(output),2)) + ' ' + output)