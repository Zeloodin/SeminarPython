#!/usr/bin/env python
# -*- coding: utf-8 -*-

import core
import string_func as strf
import action_school_grades as acgrad
import action_school_subjects as acsubj

def show_student_list(user_id):
    match core.all_get_user(user_id, 0, 1):
        case 0:  # Администратор
            strf.get_txtfile(user_id=user_id,show=True)
        case 1:  # Учитель
            strf.get_txtfile(user_id=user_id,show=True)
        case 2:  # Ученик
            strf.get_txtfile(user_id=user_id,show=True)
        case 3:  # Гость
            pass
        case _:
            pass

def add_grades_to_student(user_id):
    print("ADDDDDDDDDDDDDDDDDDD")

def select_student(user_id,find_value,parameter=0,mode_search=0):
    print()
    database = strf.get_txtfile(user_id=user_id,show=False)
    for id in database[1:]:
        is_value_int = type(find_value) == int
        is_value_list = type(find_value) == list


        try:
            is_if_0 = (int(id[parameter]) == find_value) if is_value_int else (int(id[parameter]) in list(find_value))
        except ValueError:
            is_if_0 = False

        try:
            is_if_1 = (str(id[parameter]) in list(find_value)) if is_value_list else (str(id[parameter]) == "".join(find_value))
        except ValueError:
            is_if_1 = False

        try:
            is_if_2 = (str(id[parameter]) in list(find_value)) if is_value_list else (str(id[parameter]) == "".join(find_value))
        except (ValueError, AttributeError, IndexError):
            is_if_2 = False

        try:
            is_if_3_find1 = find_value.replace(";",",").split(",")[0]
            is_if_3_1 = str(id[4]) == is_if_3_find1
        except (ValueError, AttributeError, IndexError):
            is_if_3_1 = False

        try:
            is_if_3_find2 = find_value.replace(";", ",").split(",")[1]
            is_if_3_2 = str(id[5]) == is_if_3_find2
        except (ValueError, AttributeError, IndexError):
            is_if_3_2 = False

        if is_if_0 and mode_search == 0:
            print(id[0],"	".join(id[4:6]),sep="	",end="	")
            try:
                print(id[7],sep="	", end="	")
            except IndexError:
                pass
            print()

        elif is_if_1 and mode_search == 1:
            print(id[0], "	".join(id[4:6]), sep="	", end="	")
            try:
                print(id[7], sep="	", end="	")
            except IndexError:
                pass
            print()

        elif is_if_2 and mode_search == 2:
            print(id[0], "	".join(id[4:6]), sep="	", end="	")
            try:
                print(id[7], sep="	", end="	")
            except IndexError:
                pass
            print()

        elif is_if_3_1 and is_if_3_2 and mode_search == 3:
            print(id[0], "	".join(id[4:6]), sep="	", end="	")
            try:
                print(id[7], sep="	", end="	")
            except IndexError:
                pass
            print()


def append_student(user_id,student_list):
    database = strf.get_txtfile(show=False)
    database.append(student_list)
    print(database)
    strf.save_txtfile(database)
    pass

def delete_student(user_id):
    pass


def edit_student(user_id):
    pass


def add_student_fir_name(user_id, fir_name, student_list, index = 5):
    student_list[index] = fir_name
    return student_list

def add_student_sec_name(user_id, sec_name, student_list, index = 4):
    student_list[index] = sec_name
    return student_list

def add_student_access_level(user_id, student_list, access_level = 2, index = 1):
    student_list[index] = int(access_level)
    return student_list

def add_student_login(user_id, student_list, login = "", index = 2):
    for id in strf.get_txtfile():
        if str(id)[index] == str(login):
            print(f"Этот логин: {login}, существует. Пожалуйста напишите другой логин.")
            return student_list

    student_list[index] = str(f"{student_list[0]}_{student_list[1]}") if login == "" else str(login)
    return student_list

def add_student_password(user_id, student_list, password = "", index = 3):
    student_list[index] = (f"{student_list[0]}_{student_list[1]}") if password == "" else password
    return student_list

def add_student_id_user(user_id, student_list, index = 0):
    data = strf.get_txtfile()[-1]
    student_list[index] = int(data[0])+1
    return student_list


