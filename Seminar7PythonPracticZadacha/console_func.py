from string_func import prime_mode, selected_mode
from generator_list import gen_list, gen_array

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
    result_split = list()
    for i in range(len(split_text)):
        print(text, sep="", end="\n")
        while(True):
            print(split_text[i],sep=sep,end=end)
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
            print("5 - Назад в меню")
            print("Введите число:", end=" ")
            selected_number = str(input())
        elif mode_num == 4: # 4 - заменить в справочнике
            print("")
            print("1 - Заменить по индексу")
            print("2 - Вернуться в меню")
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


if __name__ == '__main__':
    list1 = gen_list()
    list1[0] = "Sad"
    list1[1] = "Mercury"
    list1[2] = "12321-4124"
    list1[3] = "Moscow"
    list1[4] = "Eath"
    # print(list1)
    # (read_list(list1, sep="  ||  "))

    list2 = ["Иванов","Иван","01020304112911","СССР","Безопасный"]
    list3 = gen_array()
    list3[0] = list2
    list3.append(list1)
    print(read_array(list3, sep="  ||  "))