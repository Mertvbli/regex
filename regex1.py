import re
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

new_spisok = []

for name in contacts_list[1:]:
    if len(name) > 7:
        del name[7:]
    full = " ".join(name)
    fio = full.split(" ")[:3]
    name_result = fio + name[3:]
    phone_pattern = r"(8|\+7)\s*\(?(\d{3})\)?-?\s*?(\d{3})-?\s*(\d{2})-?\s*(\d{2}-?\s*)(\d*\s*)\(?([доб.]*)\s*(\d*)\)?"
    name_result[5] = re.sub(phone_pattern, r"+7(\2)\3-\4-\5\7\8", name[5])
    new_spisok.append(name_result)
    # print(name_result)


# print(new_spisok)
correct_contacts = [contacts_list[0]]
for i in new_spisok:
    l_name = i[0]
    f_name = i[1]
    for j in new_spisok:
        if l_name == j[0] and f_name == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
    if i not in correct_contacts:
        correct_contacts.append(i)

# print(correct_contacts)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')  # Вместо contacts_list подставьте свой список
    datawriter.writerows(correct_contacts)
