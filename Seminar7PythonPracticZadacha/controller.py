from console_func import input_selected_number
from list_func import *
from console_func import read_list,read_array

def run_controller():
    print("")
    print("0 - посмотреть телефонный справочник")
    print("1 - создать новый телефонный справочник")
    print("2 - добавить в телефонный справочник")
    print("3 - заменить в справочнике")
    print("4 - удалить из телефонного справочника")
    print("5 - найти в справочнике")
    print("6 - импорт справочника")
    print("7 - экспорт справочника в txt")
    print("8 - экспорт справочника в csv")
    print("9 - выход из программы")

def run_controller_00(mode_num,data_phonebook):
    print("")
    print(read_array(data_phonebook, sep="  ||  ",show=False ,get=True))
    print("Нажмите на [Enter] чтобы вернуться в меню")
    selected_number = input_selected_number(mode_num)
    return data_phonebook,selected_number

def run_controller_01(mode_num,data_phonebook):
    print("")
    print("1 - Создать новый телефонный справочник")
    print("2 - Вернуться в меню")
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

def run_controller_02(mode_num):
    print("")
    print("1 - Добавить человека в телефонный справочник")
    print("")

def run_controller_03(mode_num):
    print("1 - ")

def run_controller_04(mode_num):
    print("1 - ")

def run_controller_05(mode_num):
    print("1 - ")

def run_controller_06(mode_num):
    print("1 - ")

def run_controller_07(mode_num):
    print("1 - ")

def run_controller_08(mode_num):
    print("1 - ")

def run_controller_09(mode_num):
    print("1 - ")