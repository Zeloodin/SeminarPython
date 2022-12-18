#!/usr/bin/env python
# -*- coding: utf-8 -*-

import users as usr
import console_menu as come

def all_get_user(value,key_search,get_index = 0):
    is_only = lambda x: True if type(x) == int else False
    is_one_list = lambda x: True if type(x) == list and len(x) <= 1 else False

    for find_user in usr.data_base_ilp:
        if_value = value.lower() if type(value) != int else value
        if_key = find_user[key_search].lower() if type(find_user[key_search]) != int else find_user[key_search]
        if if_value == if_key:
            if is_one_list(get_index):
                match len(get_index):
                    case 1:
                        return find_user[get_index.pop()]
                    case 0:
                        print("Empty value")
                        return 2
            elif is_only(get_index):
                return find_user[get_index]
            else:
                return [find_user[ind] for ind in get_index]


def run():
    # | 0 - логин | 1 - пароль |
    logpas = usr.sign_in()

    #| 0 - айди | 1 - уровень доступа | 2 - логин | 3 - пароль | 4 - фамилия | 5 - имя |
    user_id,level,login,sec_name,fir_name = all_get_user(logpas[0],2,[0,1,2,4,5])

    come.menu(user_id)



# действие с учениками.             action with the students.txt.
# действие с школьными оценками.    action with school grades.
# действие с школьными предметами.  action with school subjects.

if __name__ == '__main__':
    print("Вход в информационную систему")