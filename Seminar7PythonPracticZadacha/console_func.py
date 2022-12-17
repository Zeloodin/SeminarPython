from string_func import prime_mode, selected_mode

inp_str = lambda out_text: str(input(out_text))
out_str = lambda out_text,sep = " ", end = "\n": print(out_text,sep=sep,end=end)
hello_beg = lambda beg_text,sep = " ", end = "\n": print(beg_text,sep=sep,end=end)

def input_prime_mode():
    while(True):
        print("Введите число:",end=" ")
        input_mode = str(input())
        if prime_mode(input_mode):
            break
    return int(input_mode)

def input_int(text="",sep=" ",end=" "):
    while(True):
        print(text,sep=sep, end=end)
        input_string = str(input())
        if input_string.isdigit():
            break
    return int(input_string)

def input_str(text="", sep=" ", end=" "):
    print(text, sep=sep, end=end)
    while(True):
        input_string = str(input())
        if input_string not in [";"]:
            break
    return input_string

def input_str_split(split_text, text="", sep=" ", end=" "):
    split_only = False
    if len(split_text) <= 1:
        split_only = True
    result_split = list()
    if not split_only:
        for i in range(len(split_text)):
            print(text, sep="", end="\n")
            while(True):
                print(split_text[i],sep=sep,end=end)
                input_string = str(input())
                if input_string not in [";"]:
                    break
            result_split.append(input_string)
    elif split_only:
        print(text, sep="", end="\n")
        split_text = "".join(split_text)
        while (True):
            print(split_text, sep=sep, end=end)
            input_string = str(input())
            if input_string not in [";"]:
                break
        result_split.append(input_string)
    return result_split

def input_selected_number(mode_num=0):
    while (True and mode_num != 0):
        if mode_num == 1: # 1 - создать новый телефонный справочник
            print("")
            print("1 - Создать новый телефонный справочник")
            print("2 - Вернуться в меню")
            selected_number = str(input())
        elif mode_num == 2: # 2 - добавить в телефонный справочник
            print("")
            print("1 - Добавить человека в телефонный справочник")
            print("2 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 3: # 3 - найти в справочнике
            print("")
            print("1 - Найти по индексу")
            print("2 - Найти по фамилии")
            print("3 - Найти по имени")
            print("4 - Найти по фамилии и имени")
            print("5 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 4: # 4 - заменить в справочнике
            print("")
            print("1 - Заменить по индексу")
            print("2 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 5: # 5 - удалить из телефонного справочника
            print("")
            print("1 - Удалить по индексу")
            print("2 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 6: # 6 - импорт справочника
            print("")
            print("По умолчанию импортирует из файла phonebook.csv")
            print("1 - Импортировать")
            print("2 - Импортировать как...")
            print("3 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 7: # 7 - экспорт справочника в txt
            print("")
            print("По умолчанию экспортирует/импортирует в файл phonebook.txt")
            print("1 - Экспорт")
            print("2 - Экспортировать как...")
            print("3 - Импорт")
            print("4 - Импортировать как...")
            print("5 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 8: # 8 - экспорт справочника в csv
            print("")
            print("По умолчанию экспортирует в файл phonebook.csv")
            print("1 - Экспорт")
            print("2 - Экспортировать как...")
            print("3 - Вернуться в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        else:
            print("Введите число:", end=" ")
            selected_number = str(input())

        if selected_mode(selected_number,mode_num):
            break

    else:
        input()
        selected_number = str("0")
        if selected_mode(selected_number, mode_num):
            return int(selected_number)
    return int(selected_number)


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
