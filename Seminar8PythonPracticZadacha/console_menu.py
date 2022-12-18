#!/usr/bin/env python
# -*- coding: utf-8 -*-

import users
import core
import action_students as acstud
import action_school_grades as acgrad
import action_school_subjects as acsubj

dict_menu = {"Предметы" : 100,
             "Просмотр оценок" : 90,
             "Список учеников" : 80,
             "Поиск по фамилии" : 200,
             "Поиск по имени" : 210,
             "Поиск по фамилии и имени" : 220,
             "Добавление оценки для ученика" : 2010,
             "Редактирование оценки для ученика" : 2020,
             "Удаление оценки для ученика" : 2030,
             "Выбрать ученика": 1000,
             "Добавить ученика" : 1010,
             "Редактировать ученика" : 1020,
             "Удалить ученика" : 1030,
             "Назад" : 1, "Выход" : 0}


dict_school_subjects = {
    "русский язык" : 101,
    "литература" : 102,
    "алгебра" : 103,
    "геометрия" : 104,
    "история" : 105,
    "английский язык" : 106,
    "немецкий язык" : 107,
    "физика" : 108,
    "химия" : 109,
    "биология" : 110,
    "обществознание" : 111,
    "география" : 112,
    "информатика" : 113,
    "ИЗО" : 114,
    "черчение" : 115,
    "физическая культура" : 116,
    "ОБЖ" : 117}



def input_int(print_text = "Введите целое число:",error_text = "Не правильный ввод."):
    while(True):
        try:
            print(print_text, end="")
            var = int(input())
            return var
        except ValueError:
            print(error_text)

#| 0 - айди | 1 - уровень доступа | 2 - логин | 3 - пароль | 4 - фамилия | 5 - имя |

def menu(user_id):
    global full_exit
    full_exit = False
    print("Добро пожаловать, в школьную информационную систему.")
    user_id, level, login, sec_name, fir_name = core.all_get_user(user_id, 0, [0, 1, 2, 4, 5])
    print("Вы "+("администратор" if level == 0 else "учитель" if level == 1 else "ученик" if level == 2 else "гость.")+".")
    print(f"Вы зашли под фамилией: {sec_name}, под именем: {fir_name}.")

    while(not full_exit):
        match core.all_get_user(user_id, 0, 1):
            case 0:# Администратор
                menu_list = ["Список учеников","Просмотр оценок","Выбрать ученика","Предметы","Поиск по фамилии","Поиск по фамилии и имени","Добавление оценки для ученика","Редактирование оценки для ученика","Удаление оценки для ученика","Добавить ученика","Редактировать ученика","Удалить ученика","Выход"]
            case 1: # Учитель
                menu_list = ["Список учеников","Просмотр оценок","Выбрать ученика","Предметы","Поиск по фамилии","Поиск по фамилии и имени","Добавление оценки для ученика","Редактирование оценки для ученика","Удаление оценки для ученика","Добавить ученика","Редактировать ученика","Удалить ученика","Выход"]
            case 2: # Ученик
                menu_list = ["Предметы","Поиск по фамилии","Выход"]
            case 3:  # Гость
                menu_list = ["Предметы","Выход"]
            case _:
                break

        [print(f"{i+1} - {menu_list[i]}") for i in range(len(menu_list))]

        var = input_int()
        var_menu = dict_menu.get(menu_list[var-1])

        match var_menu:
            case 0:
                full_exit = True
                break
            case 100:
                school_subjects(user_id)
            case 80:
                match core.all_get_user(user_id, 0, 1):
                    case 0, 1, 2: # Администратор
                        acstud.show_student_list(user_id)
                    case 1: # Учитель
                        acstud.show_student_list(user_id)
                    case 2:  # Ученик
                        acstud.show_student_list(user_id)
                    case 3:  # Гость
                        pass
                    case _:
                        break
            case 2010:
                match core.all_get_user(user_id, 0, 1):
                    case 0: # Администратор
                        acstud.add_grades_to_student(user_id)
                    case 1: # Учитель
                        acstud.add_grades_to_student(user_id)
            case 1000:
                match core.all_get_user(user_id, 0, 1):
                    case 0:  # Администратор
                        acstud.select_student(user_id,0)
                    case 1:  # Учитель
                        acstud.select_student(user_id,[25])

def school_subjects(user_id):
    global full_exit
    while (True):
        school_subjects_list = [i for i in dict_school_subjects]
        school_subjects_list.extend(["Назад","Выход"])
        [print(f"{i+1} - {school_subjects_list[i]}") for i in range(len(school_subjects_list))]

        var = input_int()
        school_subjects_menu = dict_menu.get(school_subjects_list[var - 1])

        match school_subjects_menu:
            case 0:
                full_exit = True
                break
            case 1:
                break














































