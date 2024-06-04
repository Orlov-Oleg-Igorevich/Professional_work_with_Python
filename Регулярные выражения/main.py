import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)[1:]


pattern = r"(\+7|8)\s*\(?(\d{3})\)?-?\s?(\d{3})-?\s?(\d{2})-?\s?(\d{2})(\s*\(?доб.\s*|)(\d+|)"
data = {}
for i, list_ in enumerate(contacts_list):
    list_data = list_[:3]
    phone = list_[5]
    if phone:
        phone = re.search(pattern, phone, flags=0)
        phone_new = f'+7({phone.group(2)}){phone.group(3)}-{phone.group(4)}-{phone.group(5)}'
        if phone.group(7):
            phone_new += f' доб.{phone.group(7)}'
        list_[5] = phone_new
    str_ = ' '.join(list_data)
    try:
        list_[0], list_[1], list_[2] = str_.split()
    except ValueError:
        list_[0], list_[1] = str_.split()
        list_[2] = ''
    finally:
        if (list_[0], list_[1]) not in data:
            data[list_[0], list_[1]] = ["" for i in range(7)]
        for j, record in enumerate(list_):
            if record:
                data[list_[0], list_[1]][j] = record

new_contacts_list = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]
new_contacts_list.extend(list(data.values()))

with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)
