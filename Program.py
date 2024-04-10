import json
import os
from datetime import datetime


def load_notes(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return []


""" Сохранение изменений в файле """
def save_notes(notes, file_name):
    with open(file_name, 'w') as file:
        json.dump(notes, file, indent=4)


""" Генерация уникальньного ID"""
def generat_unique_ID(notes):
    id = [note['id'] for note in notes]
    if id:
        return max(id) + 1
    else:
        return 1


""" Создание новой заметки """
def create_notes(notes):
    title = input("Введите заголовок: ")
    body = input("Введите текст: ")
    time_set = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    new_note = {
        'id': generat_unique_ID(notes),
        'title': title,
        'body': body,
        'time': time_set
    }
    notes.append(new_note)
    save_notes(notes, 'notes.json')
    print("Заметка успешно сохранена")


""" Просмотр заметок """
def view_notes(notes):
    if notes != []:
        for note in notes:
            print("ID:", note['id'])
            print("Заголовок:", note['title'])
            print("Текст:", note['body'])
            print("Дата создания:", note['time'])
            print()
    else:
        print("Заметки не найдены. Нажмите 1, чтобы создать первую заметку")


""" Проверка корректности введеной пользователем даты """
def correct_date(select_date):
    try:
        datetime.strptime(select_date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


""" Фильтрация по дате """
def filter_by_date(notes):
    select_date = input("Введите дату в формате 'ДД-ММ-ГГГГ': ")
    while not correct_date(select_date):
        print("Некорректный формат даты. Повторите попытку")
        select_date = input("Введите дату в формате 'ДД-ММ-ГГГГ': ")
    
    filtered_notes = [note for note in notes if note['time'].split(", ")[0] == select_date]

    if filtered_notes:
        for note in filtered_notes:
            print()
            print("Найденные заметки по дате", select_date, ":\n")
            print("ID:", note['id'])
            print("Заголовок:", note['title'])
            print("Текст:", note['body'])
            print("Дата создания:", note['time'])
            print()
    else:
        print()
        print(select_date, "В этот день вы не оставляли заметок")


""" Редактирование заметок """
def edit_notes(notes):
    select_id = int(input("Введите ID заметки, которую хотите изменить: "))
    for note in notes:
        if note['id'] == select_id:
            note['title'] = input("Введите новый заголовок: ")
            note['body'] = input("Введите новый текст: ")
            note['time'] = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            save_notes(notes, 'notes.json')
            print("Заметка успешно изменена")
            return
    print("ID не найден. Введите корректный ID")


""" Удаление заметок """
def delete_notes(notes):
    select_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == select_id:
            notes.remove(note)
            save_notes(notes, 'notes.json')
            print("Заметка успешно удалена")
        else:
            print("ID не найден. Введите корректный ID")


def main():
    
    notes = load_notes('notes.json')

    flag = True
    while flag:
        print("\n0 - Выход")
        print("1 - Создать")
        print("2 - Просмотреть")
        print("3 - Просмотреть с учетом фильтрации по дате")
        print("4 - Редактировать")
        print("5 - Удалить\n")
        answer = input("Выберите действие: ")
        print()

        if answer == "0":
            flag = False

        elif answer == "1":
            create_notes(notes)

        elif answer == "2":
            view_notes(notes)

        elif answer == "3":
            filter_by_date(notes)

        elif answer == "4":
            edit_notes(notes)

        elif answer == "5":
            delete_notes(notes)
            
        else:
            print("Неверно введено действие, проверьте написание")


if __name__ == '__main__':
    main()
