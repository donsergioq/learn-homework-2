"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


employee_list = [
    {
        'name': 'John Doe',
        'age': 25,
        'job': 'Manager'
    },
    {
        'name': 'Alice Cooper',
        'age': 27,
        'job': 'Accountant'
    },
    {
        'name': 'Joe Shmoe',
        'age': 21,
        'job': 'Technician'
    },
    {
        'name': 'Tom Harris',
        'age': 22,
        'job': 'Engineer'
    },
    {
        'name': 'Dick Thompson',
        'age': 27,
        'job': 'Programmer'
    }
]


def main():
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for employee in employee_list:
            writer.writerow(employee)


if __name__ == "__main__":
    main()
