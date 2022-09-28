from pprint import pprint
import re
import csv


with open('phonebook_raw.csv') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


def name_sort():
    for group in contacts_list[1:]:
        string = group[0] + group[1] + group[2]
        if len((re.sub(r'([А-Я])', r' \1', string).split())) == 3:
            group[0] = re.sub(r'([А-Я])', r' \1', string).split()[0]
            group[1] = re.sub(r'([А-Я])', r' \1', string).split()[1]
            group[2] = re.sub(r'([А-Я])', r' \1', string).split()[2]
        elif len((re.sub(r'([А-Я])', r' \1', string).split())) == 2:
            group[0] = re.sub(r'([А-Я])', r' \1', string).split()[0]
            group[1] = re.sub(r'([А-Я])', r' \1', string).split()[1]
            group[2] = ''
        elif len((re.sub(r'([А-Я])', r' \1', string).split())) == 1:
            group[0] = re.sub(r'([А-Я])', r' \1', string).split()[0]
            group[1] = ''
            group[2] = ''



def phone_number():
    pattern = re.compile(
        r'(\+7|8)\s?[/(]?(\d{3})[/)]?\s?\D?(\d{3})[/-]?(\d{2})[/-]?(\d{2})((\s)?[/(]?(доб.)?\s?(\d+)[/)]?)?')
    for group in contacts_list:
        group[5] = pattern.sub(r'+7(\2)\3-\4-\5\7\8\9', group[5])



def merge_list():
    count = 0
    while count <= len(contacts_list) - 1:
        p = contacts_list[count]
        for i in contacts_list[count + 1:]:
            if p[0] == i[0] and p[1] == i[1]:
                count_2 = 0
                while count_2 <= 6:
                    if len(p[count_2]) < len(i[count_2]):
                        p[count_2] = i[count_2]
                    count_2 += 1
                contacts_list.remove(i)
        count += 1


if __name__ == '__main__':
    name_sort()
    phone_number()
    merge_list()

with open('phonebook.csv', 'w') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)