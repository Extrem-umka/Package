import re
# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# 1.поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке
# изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# 2.привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой:
# +7(999)999-99-99 доб.9999;
# 3.объединить все дублирующиеся записи о человеке в одну.

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
from pprint import pprint

def read_csv():
  with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
#
def phone_number(contacts_list):
  number_pattern = r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})(?:\s*\(*(доб\.)\s*(\d{4})|)\)?"
  contacts_list_up = list()
  for cont in contacts_list:
    cont_str = ",".join(cont)
    result = re.sub(number_pattern, r"+7(\2)\3-\4-\5 \6\7", cont_str)
    cont_str = result.split(',')
    contacts_list_up.append(cont_str)
  return contacts_list_up


def fio(contacts_list):
  name_pattern = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
  contacts_list_up = list()
  for cont in contacts_list:
    cont_str = ','.join(cont)
    result = re.sub(name_pattern, r"\1\3\10\4\6\9\7\8", cont_str)
    cont_str = result.split(',')
    contacts_list_up.append(cont_str)
  return contacts_list_up

def union(contacts_list):
  for i in contacts_list:
    for j in contacts_list:
      if i[0] == j[0] and i[1] == j[1] and i is not j:
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
  contacts_list_up = list()
  for cont in contacts_list:
    if cont not in contacts_list_up:
      contacts_list_up.append(cont)
  return contacts_list_up

# # TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def write_csv(contacts_list):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)

if __name__ == '__main__':
  contrlist = read_csv()
  contrlist = phone_number(contrlist)
  contrlist = fio(contrlist)
  contrlist = union(contrlist)
  write_csv(contrlist)

