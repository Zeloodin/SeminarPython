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

def select_student(user_id,find_value,parameter=0):
    print()
    database = strf.get_txtfile(user_id=user_id,show=False)
    for id in database:
        try:
            is_value_int = type(find_value) == int
            if ((int(id[0]) == find_value) if is_value_int else (int(id[0]) in list(find_value))) and parameter==0:
                print(id[0],"	".join(id[4:6]),sep="	",end="	")
                try:
                    print(id[7],sep="	", end="	")
                except IndexError: pass
                print()
        except ValueError: pass
    print()
