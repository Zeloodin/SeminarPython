from constant import cells_per_user
from list_func import *

def get_txtfile(name = "phonebook.txt",split='\n',sep =";",end='\n', show = False, show_sep="  ||  ", show_end='\n'):
    try:
        try:
            with open(name, "r", encoding = 'windows-1251') as f:
                open_txt = (f.read()).split(split)
        except UnicodeDecodeError:
            with open(name, "r", encoding = 'utf-8') as f:
                open_txt = (f.read()).split(split)

        string_text = ""

        for i in range(len(open_txt)):
            if open_txt[i] == "": pass
            elif i % cells_per_user == cells_per_user-1:
                if show:
                    print(open_txt[i], end=show_end)
                string_text = string_text + open_txt[i] + end
            else:
                if show:
                    print(open_txt[i], end=show_sep)
                string_text = string_text + open_txt[i] + sep

        return string_text

    except FileNotFoundError: print(f"Отсутствует файл {name}")

def save_txtfile(data,name = "phonebook.txt",split='\n',sep =";",end='\n', show = False, show_sep="  ||  ", show_end='\n'):
    try:
        data = data.replace(";","\n")
        try:
            with open(name, "w", encoding = 'utf-8') as f:
                f.write(data)
        except UnicodeDecodeError:
            with open(name, "w", encoding = 'windows-1251') as f:
                f.write(data)

    except FileNotFoundError: print(f"Отсутствует файл {name}")

def list_to_str_data(data, sep =";", end='\n'):
    string_text = ""

    for i in range(len(data)):
        for j in range(len(data[i])):
            string_text = string_text + data[i][j] + sep
    return string_text

def str_to_list_data(data, split=';', sep =";", end='\n'):
    open_txt = data.split(split)
    first = []
    second_all = []
    for i in range(len(open_txt)//cells_per_user):
        for j in range(cells_per_user):
            first.append(open_txt[i*cells_per_user+j])
        second_all.append(first)
        first = []
    return second_all


if __name__ == '__main__':
    from csv_func import *
    arr1 = get_txtfile("1.csv",split=";",sep="\n",end="\n")

    save_txtfile(list_to_str_data(get_csvfile()),"1222.txt")

    a1 = list_to_str_data(get_csvfile())
    print(a1)

    a2 = str_to_list_data(a1)
    print(a2)

    pass