#!/usr/bin/env python
# -*- coding: utf-8 -*-

import users
import core
import action_students as acstud
import action_school_grades as acgrad
import action_school_subjects as acsubj
import string_func as srtf


def input_int(print_text = "Введите целое число:",error_text = "Не правильный ввод."):
    while(True):
        try:
            print(print_text, end="")
            var = int(input())
            return var
        except ValueError:
            print(error_text)

def input_str(print_text = "Введите слово:",error_text = "Не правильный ввод."):
    while(True):
        try:
            print(print_text, end="")
            var = str(input())
            return var
        except ValueError:
            print(error_text)

def input_int_list(count=1,print_text = "Введите целые числа через запятую, или через точку с запятой:",error_text = "Не правильный ввод."):
    while(True):
        list_input = []
        try:
            print(print_text, end="")
            var = str(input())
            [list_input.append(int(n)) for n in var.replace(",",";").split(";")]
            return list_input
        except ValueError:
            print(error_text)

def input_str_list(count=1,print_text = "Введите слова через запятую, или через точку с запятой:",error_text = "Не правильный ввод."):
    while(True):
        list_input = []
        try:
            print(print_text, end="")
            var = str(input())
            [list_input.append(str(n)) for n in var.replace(",",";").split(";")]
            return list_input
        except ValueError:
            print(error_text)


dict_menu = {"Предметы" : 100,
             "Просмотр оценок" : 90,
             "Список учеников" : 80,
             # "Поиск по фамилии" : 200,
             # "Поиск по имени" : 210,
             # "Поиск по фамилии и имени" : 220,
             "Добавление оценки для ученика" : 2010,
             "Редактирование оценки для ученика" : 2020,
             "Удаление оценки для ученика" : 2030,
             "Выбрать ученика": 1000,
             "Добавление, редактирование, удаление ученика": 1100,
             # "Добавить ученика" : 1010,
             # "Редактировать ученика" : 1020,
             # "Удалить ученика" : 1030,
             "Назад" : 1, "Выход" : 0}


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
                menu_list = ["Список учеников","Просмотр оценок","Выбрать ученика","Предметы","Добавление оценки для ученика","Редактирование оценки для ученика","Удаление оценки для ученика","Добавление, редактирование, удаление ученика","Назад","Выход"]
            case 1: # Учитель
                menu_list = ["Список учеников","Просмотр оценок","Выбрать ученика","Предметы","Добавление оценки для ученика","Редактирование оценки для ученика","Удаление оценки для ученика","Добавление, редактирование, удаление ученика","Назад","Выход"]
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
                menu_school_subjects(user_id)
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
                        menu_select_student(user_id)
                    case 1:  # Учитель
                        menu_select_student(user_id)
            case 1100:
                match core.all_get_user(user_id, 0, 1):
                    case 0:  # Администратор
                        menu_add_edt_del_student(user_id)
                    case 1:  # Учитель
                        menu_add_edt_del_student(user_id)

# ----------------------------------------------------------------------------------------------------------------------

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



def menu_school_subjects(user_id):
    global full_exit
    while(not full_exit):
        menu_school_subjects_list = [i for i in dict_school_subjects]
        menu_school_subjects_list.extend(["Назад","Выход"])
        [print(f"{i+1} - {menu_school_subjects_list[i]}") for i in range(len(menu_school_subjects_list))]

        var = input_int()
        menu_school_subjects_var = dict_menu.get(menu_school_subjects_list[var - 1])

        match menu_school_subjects_var:
            case 0:
                full_exit = True
                break
            case 1:
                break

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------

dict_menu_select_student = {
    "По id" : 5000,
    "По фамилии" : 5010,
    "По имени" : 5020,
    "По фамилии и имени" : 5030,
    "Назад" : 1,
    "Выход" : 0}

def menu_select_student(user_id):
    global full_exit
    while (not full_exit):
        print()
        print("Выберите ученика(ов)")
        menu_select_student_list = [i for i in dict_menu_select_student]
        [print(f"{i + 1} - {menu_select_student_list[i]}") for i in range(len(menu_select_student_list))]

        var = input_int()
        menu_select_student_var = dict_menu_select_student.get(menu_select_student_list[var - 1])

        match menu_select_student_var:
            case 5000:
                acstud.select_student(user_id, input_int_list(), parameter=0, mode_search=0)
            case 5010:
                acstud.select_student(user_id, input_str_list(), parameter=4, mode_search=1)
            case 5020:
                acstud.select_student(user_id, input_str_list(), parameter=5, mode_search=2)
            case 5030:
                acstud.select_student(user_id, input_str(), mode_search=3)

            case 1:
                break
            case 0:
                full_exit = True
                break

# ----------------------------------------------------------------------------------------------------------------------

dict_menu_add_edt_del_student = {
    "Добавить ученика" : 6000,
    "Редактировать ученика" : 6010,
    "Удалить ученика" : 6020,
    "Назад" : 1,
    "Выход" : 0}

def menu_add_edt_del_student(user_id):
    global full_exit
    while (not full_exit):
        print()
        print("Выберите действие")
        menu_add_edt_del_student_list = [i for i in dict_menu_add_edt_del_student]
        [print(f"{i + 1} - {menu_add_edt_del_student_list[i]}") for i in range(len(menu_add_edt_del_student_list))]

        var = input_int()
        menu_add_edt_del_student_var = dict_menu_add_edt_del_student.get(menu_add_edt_del_student_list[var - 1])

        match menu_add_edt_del_student_var:
            case 6000:
                menu_add_student(user_id)
            case 6010:
                pass
            case 6020:
                pass

            case 1:
                break
            case 0:
                full_exit = True
                break

dict_menu_add_student = {
    "Добавить Имя" : 7000,
    "Добавить Фамилию" : 7010,
    "Добавить Логин" : 7020,
    "Добавить Пароль": 7030,
    # "Добавить Класс" : 7040,
    "Сохранить": 7050,
    "Назад" : 1,
    "Выход" : 0}

def menu_add_student(user_id):
    global full_exit
    student_list = ["" for i in range(srtf.get_txtfile_lenghtrow())]

    student_list = acstud.add_student_id_user(user_id=user_id,student_list=student_list)
    student_list = acstud.add_student_access_level(user_id=user_id,student_list=student_list,access_level=2)
    student_list = acstud.add_student_login(user_id=user_id,student_list=student_list)
    student_list = acstud.add_student_password(user_id=user_id,student_list=student_list)

    while (not full_exit):
        print(student_list)
        print()
        print("Добавление ученика\nВыберите действие")
        menu_add_student_list = [i for i in dict_menu_add_student]
        [print(f"{i + 1} - {menu_add_student_list[i]}") for i in range(len(menu_add_student_list))]

        var = input_int()
        menu_add_student_var = dict_menu_add_student.get(menu_add_student_list[var - 1])

        match menu_add_student_var:
            case 7000:
                student_list = acstud.add_student_fir_name(user_id=user_id,fir_name=input_str(print_text="Введите имя:"),student_list=student_list)
            case 7010:
                student_list = acstud.add_student_sec_name(user_id=user_id, sec_name=input_str(print_text="Введите фамилию:"), student_list=student_list)
            case 7020:
                student_list = acstud.add_student_login(user_id=user_id, login=input_str(print_text="Введите логин:"), student_list=student_list)
            case 7030:
                student_list = acstud.add_student_password(user_id=user_id, password=input_str(print_text="Введите пароль:"), student_list=student_list)
            case 7040:
                pass
            case 7050:
                acstud.append_student(user_id=user_id, student_list=student_list)

            case 1:
                break
            case 0:
                full_exit = True
                break































