import csv
import re

def get_data(llist):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [[]]
    for i in range(len(llist)):
        with open(llist[i]) as file:
            data = csv.reader(file)
            for row in data:
                names = row[0].split(':')
                if  re.search('Изготовитель системы',names[0]):
                    os_prod_list.append(" ".join(names[1].split()))
                    if not names[0] in main_data[0]:
                        main_data[0].append(names[0])
                if re.search('Название ОС',names[0]):
                    os_name_list.append(" ".join(names[1].split()))
                    if not names[0] in main_data[0]:
                        main_data[0].append(names[0])
                if re.search('Код продукта',names[0]):
                    os_code_list.append(" ".join(names[1].split()))
                    if not names[0] in main_data[0]:
                        main_data[0].append(names[0])
                if re.search('Тип системы', names[0]):
                    os_type_list.append(" ".join(names[1].split()))
                    if not names[0] in main_data[0]:
                        main_data[0].append(names[0])

    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_prod_list)
    main_data.append(os_type_list)
    return main_data


def write_to_csv(link,llist):
    data = get_data(llist)
    with open(link, 'w') as file:
        wr_data = csv.writer(file)
        for row in data:
            wr_data.writerow(row)

write_to_csv('result.csv',['info_1.txt','info_2.txt','info_3.txt'])
with open('result.csv') as f_n:
    print(f_n.read())
