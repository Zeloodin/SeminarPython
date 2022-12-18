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
        except ValueError:
            is_if_2 = False

        try:
            is_if_3_find1 = find_value.replace(";",",").split(",")[0]
            is_if_3_1 = str(id[4]) == is_if_3_find1
        except ValueError:
            is_if_3_1 = False

        try:
            is_if_3_find2 = find_value.replace(";", ",").split(",")[1]
            is_if_3_2 = str(id[5]) == is_if_3_find2
        except ValueError:
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

