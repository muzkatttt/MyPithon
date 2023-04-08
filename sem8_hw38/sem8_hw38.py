"""
Задача 38: Дополнить телефонный справочник возможностью
изменения и удаления данных. Пользователь также может
ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.

Cоздать телефонный справочник с возможностью импорта и
экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска
определенной записи(Например имя или фамилию человека)
Create, Read, Update, Delete
"""

import json
import os


# создать контакт в телефонной книге Create
def create_person(persons: list) -> None:
    person = dict(
        first_name=input(f'Введите имя:\n'),
        second_name=input(f'Введите фамилию:\n'),
        phone=input(f'Введите номер телефона:\n')
    )
    persons.append(person)


def dump(persons):  # сохранение
    with open('persons.json', 'w', encoding='UTF-8') as f:
        json.dump(persons, f, ensure_ascii=False)


def load(): # чтение
    with open('persons.json', 'r', encoding='UTF-8') as f:
        persons = json.load(f)
    return persons


def print_phonebook(entity):
    print(f'{entity}')


def find_contact(contacts: list) -> list: # можно создать проверку наличия значений
    what = input('Кого ищем?\n>>> ')
    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        return found
    else:
        print('Никого не нашли ;(')
        return list()


def func_pop(persons: list) -> None:
    who_delete = find_contact(persons)[0]
    print(persons.pop(persons.index(who_delete)))


def func_change(persons: list) -> None: # можно создать проверку наличия значений
    who_change = find_contact(persons)[0]
    print(who_change)
    save_key = input('Введите ключ:\n')
    who_change[save_key] = input('Введите новое значение: \n')
    print(who_change)


def get_commands() -> dict:
    return {
        'Создать': create_person,
        'Найти': find_contact,
        'Показать': print_phonebook,
        'Изменить': func_change,
        'Удалить': func_pop,
        'Завершить': 0
    }


def menu(phonebook: list) -> int:
    commands = get_commands()
    numerated_list = list(enumerate(commands, 1))
    print('Выберите команду по номеру:',
          '\n'.join(f'{num}. {key}' for num, key in numerated_list), sep='\n')
    choice = input('>>> ')
    command_index = int(choice) - 1
    if func := commands[numerated_list[command_index][1]]:
        if value := func(phonebook):
            print_phonebook(value)
        return 1
    return 0


def main():
    phonebook = load()  # первая функция в мэйн
    while menu(phonebook):
        pass
    dump(phonebook)  # обязательно последняя


if __name__ == '__main__':
    main()
