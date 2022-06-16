from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


new_contacts_list = []
pattern_number = "(\+7|8)*[\s\(]*(\d{3})[\))\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})(\s)*(\()*(доб.)*[\s]*(\d+)*[\)]*"
new_number = r'+7(\2)\3-\4-\5\6\8\9'
def main(contacts_list):
    for contact in contacts_list:
        name = ' '.join(contact[:3]).split(' ')
        new_list = [name[0], name[1], name[2], contact[3], contact[4], re.sub(pattern_number, new_number, contact[5]), contact[6]]
        new_contacts_list.append(new_list)
    return merge(new_contacts_list)


def merge(contacts):
    for contact in contacts:
        for new_contact in contacts:
            if contact[0] == new_contact[0] and contact[1] == new_contact[1]:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    new_list = []
    for i in contacts:
        if i not in new_list:
            new_list.append(i)
    return new_list


with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(main(contacts_list))
