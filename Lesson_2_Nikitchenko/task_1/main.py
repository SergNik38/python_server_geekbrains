"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re
from chardet import detect


def get_data():
    manufacturer_list = []
    os_name_list = []
    prod_code_list = []
    os_type_list = []
    headers = ['№ п/п', 'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = []

    main_data.append(headers)
    for i in range(1, 4):
        file = open(f'info_{i}.txt', 'rb')
        data = file.read()
        detected = detect(data)
        # на маке возникла проблема с чтением из-за кодировки, пришлось декодировать
        text_content = data.decode(detected['encoding'])
        manufacturer = re.compile(r'Изготовитель системы:(.*?)\n')
        manufacturer_list.append(' '.join(manufacturer.findall(text_content)[0].split()))

        os_name = re.compile(r'Название ОС:(.*?)\n')
        os_name_list.append(' '.join(os_name.findall(text_content)[0].split()))

        prod_code = re.compile(r'Код продукта:(.*?)\n')
        prod_code_list.append(' '.join(prod_code.findall(text_content)[0].split()))

        os_type = re.compile(r'Тип системы:(.*?)\n')
        os_type_list.append(' '.join(os_type.findall(text_content)[0].split()))

    j = 1
    for i in range(0, 3):
        row_data = []
        row_data.append(j)
        row_data.append(manufacturer_list[i])
        row_data.append(os_name_list[i])
        row_data.append(prod_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)
        j += 1
    return main_data


def write_to_csv(result):
    data = get_data()
    with open(result, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)


write_to_csv('data_report.csv')
