import re
import chardet
import csv


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        with open(f'info_{i}.txt', 'rb') as file_obj:
            data_bytes = file_obj.read()
            result = chardet.detect(data_bytes)
            data = data_bytes.decode(result['encoding'])

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_reg.findall(data)[0].split()[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    headers = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    main_data.append(headers)

    data_for_rows = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for idx in range(len(data_for_rows[0])):
        line = [row[idx] for row in data_for_rows]
        main_data.append(line)

    return main_data


get_data()


def write_to_csv(out_file):
    main_data = get_data()
    with open(out_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)
            

write_to_csv('data_report.csv')

# изначально решил так: потом посмотрел разбор и переделал
# list_of_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
#
#
# def get_data():
#     os_prod_list = []
#     os_name_list = []
#     os_code_list = []
#     os_type_list = []
#     main_data = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
#     for file in list_of_files:
#         with open(file, encoding='windows-1251') as f_n:
#             for row in f_n:
#                 if 'Изготовитель системы' in row:
#                     os_prod_list.append(row[len('Изготовитель системы')+1:].strip())
#                     print(row)
#                 if 'Название ОС' in row:
#                     os_name_list.append(row[len('Название ОС') + 1:].strip())
#                     print(row)
#                 if 'Код продукта' in row:
#                     os_code_list.append(row[len('Код продукта') + 1:].strip())
#                     print(row)
#                 if 'Тип системы' in row:
#                     os_type_list.append(row[len('Тип системы') + 1:].strip())
#                     print(row)
#         print('-' * 80)
#         print(os_prod_list)
#         print(os_name_list)
#         print(os_code_list)
#         print(os_type_list)
#         data = [os_prod_list, os_name_list, os_code_list, os_type_list, main_data]
#         print(data)
#
#
# get_data()

