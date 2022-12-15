from console_func import input_selected_number, read_list, read_array, input_int, input_str, input_str_split
from list_func import *
from csv_func import save_csvfile, read_csvfile, get_csvfile
from list_func import append_user
from txt_func import str_to_list_data, list_to_str_data, save_txtfile, get_txtfile


def run_controller():
    print("")
    print("0 - посмотреть телефонный справочник")
    print("1 - создать новый телефонный справочник")
    print("2 - добавить в телефонный справочник")
    print("3 - найти в справочнике")
    print("4 - заменить в справочнике")
    print("5 - удалить из телефонного справочника")
    print("6 - импорт справочника")
    print("7 - экспорт/импорт справочника в txt")
    print("8 - экспорт справочника в csv")
    print("9 - выход из программы")

def run_controller_00(mode_num, data_phonebook): # 0 - посмотреть телефонный справочник
    print("")
    print(read_array(data_phonebook, sep="  ||  ",show=False ,get=True))
    print("Нажмите на [Enter] чтобы вернуться в меню")
    selected_number = input_selected_number(mode_num)
    return data_phonebook,selected_number

def run_controller_01(mode_num, data_phonebook): # 1 - создать новый телефонный справочник
    # print("")
    # print("1 - Создать новый телефонный справочник")
    # print("2 - Вернуться в меню")
    while(True):
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Создан новый телефонный справочник")
            data_phonebook = list()
            return data_phonebook,selected_number
        elif selected_number == 2:
            print()
            print("Назад в меню")
            return data_phonebook,selected_number

def run_controller_02(mode_num, data_phonebook): # 2 - добавить в телефонный справочник
    # print("")
    # print("1 - Добавить человека в телефонный справочник")
    # print("2 - Вернуться в меню")
    while(True):
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Добавить в телефонный справочник")
            data_phonebook = append_user(data_phonebook)
        elif selected_number == 2:
            print()
            print("Назад в меню")
            return data_phonebook,selected_number

def run_controller_03(mode_num, data_phonebook): # 3 - найти в справочнике
    # print("")
    # print("1 - Найти по индексу")
    # print("2 - Найти по фамилии")
    # print("3 - Найти по имени")
    # print("4 - Найти по фамилии и имени")
    # print("5 - Назад в меню")
    print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
    while (True):
        selected_number = input_selected_number(mode_num)
        if selected_number == 1: # 1 - Найти по индексу
            print()
            print("Введите индекс: ",end="")
            find_to_data(data_phonebook,selected_number,input_str())

        if selected_number == 2: # 2 - Найти по фамилии
            print()
            print("Введите фамилию: ",end="")
            find_to_data(data_phonebook,selected_number,input_str())

        if selected_number == 3: # 3 - Найти по имени
            print()
            print("Введите имя: : ",end="")
            find_to_data(data_phonebook,selected_number,input_str())

        if selected_number == 4: # 4 - Найти по фамилии и имени
            print()
            # print("Введите фамилию и имя: ",end="")
            string_print = ["Введите фамилию: ","Введите имя: "]
            find_to_data(data_phonebook,selected_number,input_str_split(string_print))

        elif selected_number == 5: # 5 - Назад в меню
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number

def run_controller_04(mode_num, data_phonebook): # 4 - заменить в справочнике
    # print("")
    # print("1 - Заменить по индексу")
    # print("2 - Вернуться в меню")
    while (True):
        print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Заменить по индексу")
            replace_index_to_data(data_phonebook)

        elif selected_number == 2:
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number

def run_controller_05(mode_num, data_phonebook): # 5 - удалить из телефонного справочника
    # print("")
    # print("1 - Удалить по индексу")
    # print("2 - Назад в меню")
    print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
    while (True):
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Удалить по индексу")
            delete_index_to_data(data_phonebook)

        elif selected_number == 2:
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number


def run_controller_06(mode_num, data_phonebook): # 6 - импорт справочника
    # print("")
    # print("По умолчанию импортирует из файла phonebook.csv")
    # print("1 - Импортировать")
    # print("2 - Импортировать как...")
    # print("3 - Вернуться в меню")
    while (True):
        print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Импортировать из phonebook.csv")
            get_data = get_csvfile()
            data_phonebook = get_data

        elif selected_number == 2:
            print()
            print("Импортировать как...")
            string_print = ["Введите название файла для импорта:"]
            name = "".join(input_str_split(string_print))
            get_data = get_csvfile(name)
            data_phonebook = get_data

        elif selected_number == 3:
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number

def run_controller_07(mode_num, data_phonebook): # 7 - экспорт/импорт справочника в txt
    # print("")
    # print("По умолчанию экспортирует/импортирует в файл phonebook.txt")
    # print("1 - Экспорт")
    # print("2 - Экспортировать как...")
    # print("3 - Импорт")
    # print("4 - Импортировать как...")
    # print("5 - Вернуться в меню")
    while (True):
        print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
        selected_number = input_selected_number(mode_num)

        if selected_number == 1:
            print()
            print("Экспортировать в phonebook.txt")
            save_txtfile(list_to_str_data(data_phonebook))

        elif selected_number == 2:
            print()
            print("Экспортировать как..")
            string_print = ["Введите название файла для экспорта:"]
            name = "".join(input_str_split(string_print))
            save_txtfile(list_to_str_data(data_phonebook),name)

        elif selected_number == 3:
            print()
            print("Импортировать из phonebook.txt")
            get_data = str_to_list_data(get_txtfile(split="\n"))
            print(get_data)
            data_phonebook = get_data

        elif selected_number == 4:
            print()
            print("Импортировать как...")
            string_print = ["Введите название файла для импорта:"]
            name = "".join(input_str_split(string_print))
            get_data = get_csvfile(name)
            data_phonebook = get_data

        elif selected_number == 5:
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number

def run_controller_08(mode_num, data_phonebook): # 8 - экспорт справочника в csv
    # print("")
    # print("По умолчанию экспортирует в файл phonebook.csv")
    # print("1 - Экспорт")
    # print("2 - Экспортировать как...")
    # print("3 - Вернуться в меню")
    while (True):
        print(read_array(data_phonebook, sep="  ||  ", show=False, get=True))
        selected_number = input_selected_number(mode_num)
        if selected_number == 1:
            print()
            print("Экспортировать в phonebook.csv")
            save_csvfile(data_phonebook)

        elif selected_number == 2:
            print()
            print("Экспортировать как..")
            string_print = ["Введите название файла для экспорта:"]
            name = "".join(input_str_split(string_print))
            save_csvfile(data_phonebook,name)

        elif selected_number == 3:
            print()
            print("Вернуться в меню")
            return data_phonebook, selected_number

def run_controller_09(mode_num, data_phonebook): # 9 - выход из программы
    print("1 - ")