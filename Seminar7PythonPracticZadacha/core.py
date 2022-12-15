from csv_func import *
from string_func import *
from console_func import *
from constant import *
from controller import *
from generator_list import *
from csv_func import *
from list_func import *
from logger import *
from math_func import *

def run_core():
    exit = False
    data_phonebook = []
    data_phonebook = get_csvfile()
    while(exit != True):
        run_controller()
        mode_num = input_prime_mode()



        match mode_num:
            case 0:  # 0 - посмотреть телефонный справочник
                data_phonebook, selected_number = run_controller_00(mode_num, data_phonebook)

            case 1: # 1 - создать новый телефонный справочник
                data_phonebook, selected_number = run_controller_01(mode_num,data_phonebook)

            case 2: # 2 - добавить в телефонный справочник
                data_phonebook, selected_number = run_controller_02(mode_num,data_phonebook)

            case 3: # 3 - заменить в справочнике
                data_phonebook, selected_number = run_controller_03(mode_num,data_phonebook)

            case 4: # 4 - удалить из телефонного справочника
                data_phonebook, selected_number = run_controller_04(mode_num,data_phonebook)

            case 5: # 5 - найти в справочнике
                data_phonebook, selected_number = run_controller_05(mode_num,data_phonebook)

            case 6: # 6 - импорт справочника
                data_phonebook, selected_number = run_controller_06(mode_num,data_phonebook)

            case 7: # 7 - экспорт справочника в txt
                data_phonebook, selected_number = run_controller_07(mode_num,data_phonebook)

            case 8: # 8 - экспорт справочника в csv
                data_phonebook, selected_number = run_controller_08(mode_num,data_phonebook)

            case 9: # 9 - выход из программы
                # data_phonebook,selected_number = run_controller_09(mode_num,data_phonebook)
                exit = True
                pass












