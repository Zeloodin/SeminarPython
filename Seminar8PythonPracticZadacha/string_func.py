#!/usr/bin/env python
# -*- coding: utf-8 -*-


import core

def read_list(list1,sep=" ", end=" ", show = True, get = False):
    if get:
        text = ""
    for i in range(len(list1)):
        if show:
            print(list1[i],sep=sep,end=end)
        if get:
            text = text + (sep if i != 0 else "") + list1[i]
    if get:
        text = text + end
    if show:
        print()
    if get:
        return text

def read_array(array1,sep=" ", end_str=" ", end_list="\n", show = True, get = False):
    if get:
        array_list = ""
    for l in range(len(array1)):
        for i in range(len(array1[l])):
            if show:
                print(array1[l][i], sep=sep, end=end_str if i >= len(array1[l])-1 else sep)
            if get:
                array_list = array_list + (sep if i != 0 else "") + array1[l][i]
        if get:
            array_list = array_list + end_list
        if show:
            print()
    if get:
        return array_list

def list_to_str_data(data, sep =";", end='\n'):
    string_text = ""

    for i in range(len(data)):
        for j in range(len(data[i])):
            string_text = string_text + data[i][j] + sep
    return string_text

def get_txtfile_lenghtrow(name = "data_base_school_users.txt",split='\n',splitrow=';'):
    try:
        try:
            with open(name, "r", encoding='windows-1251') as f:
                open_txt = (f.read()).split(split)
                open_txt = open_txt[0].split(splitrow)
        except UnicodeDecodeError:
            with open(name, "r", encoding='utf-8') as f:
                open_txt = (f.read()).split(split)
                open_txt = open_txt[0].split(splitrow)
        lenght_0pen_txt = len(open_txt)
        return lenght_0pen_txt
    except FileNotFoundError:
        print(f"Отсутствует файл {name}")



def save_txtfile(data,name = "data_base_school_users.txt",split='\n',sep =";",end='\n', show = False, show_sep="  ||  ", show_end='\n'):
    print(data)
    try:

        with open(name, "w", encoding = 'utf-8') as f:
            f.write("")
        with open(name, "a+", encoding = 'windows-1251') as f:
            for i in range(len(data)):

                for j in range(len(data[i])):
                    if type(data[i][j]) not in [dict,list]:
                        data[i][j] = str(data[i][j])

                try:

                    f.write(str(";".join(data[i])))
                except TypeError:
                    continue
                f.write("\n")


    except FileNotFoundError:
        print(f"Отсутствует файл {name}")



def get_txtfile(name = "data_base_school_users.txt",split='\n',sep =";",end='\n', show = False, show_sep="  ||  ", show_end='\n', user_id=None):
    try:
        try:
            with open(name, "r", encoding = 'windows-1251') as f:
                open_txt = (f.read()).split(split)
        except UnicodeDecodeError:
            with open(name, "r", encoding = 'utf-8') as f:
                open_txt = (f.read()).split(split)

        for i in range(len(open_txt)):
            if open_txt[i] == "": open_txt.pop(i)
            else:
                open_txt[i]=(open_txt[i]).split(";")
        if show:
            for j in range(len(open_txt)):
                if j == 0:
                    pass
                else:
                    level_show = lambda x=int(open_txt[j][1]): ["Администратор", "Учитель", "Ученик", "Гость", "Никто"][x]
                    if user_id != None:
                        match core.all_get_user(user_id, 0, 1):
                            case 0: # Администратор
                                print("	".join(open_txt[j][0:1]), level_show(), "	".join(open_txt[j][1:]), sep="	")
                            case 1: # Учитель
                                if int(open_txt[j][1]) in [2, 1, 0]:
                                    print("	".join(open_txt[j][0:1]),level_show(), "	".join(open_txt[j][4:6]), sep="	")
                            case 2: # Ученик
                                if int(open_txt[j][1]) in [2, 1]:
                                    print(level_show(),"	".join(open_txt[j][4:6]),sep="	")
                            case 3: # Гость
                                if int(open_txt[j][1]) in [3, 4]:
                                    print(level_show(),"	".join(open_txt[j][5:6]),sep="	")
                            case _:
                                pass
                    else:
                        print(level_show(),"	".join(open_txt[j][4:6]),sep="	")



        return open_txt

    except FileNotFoundError: print(f"Отсутствует файл {name}")