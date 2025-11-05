import csv


def write_rows_to_csv(filename, rows):
    with open(filename, mode='w',newline='', encoding='utf-8') as file:
        # Создаем объект для записи данных в csv
        writer = csv.writer(file)
        # Запись первой строки с названием колонн
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
    return dict
