from generator_list import gen_list
from constant import cells_per_user, dict_us, list_user, list_user_kir
from console_func import inp_str, out_str, input_int
from string_func import filter_text
from csv_func import save_csvfile, read_csvfile, get_csvfile

def get_dict_keys(dict):
    return [n for n in dict.keys()]

def get_dict_values(dict):
    return [n for n in dict.values()]

def get_dict_items(dict):
    return [n for n in dict.items()]

def append_user(data_users = None, id = None):
    user_list = gen_list()
    i = 0
    all_list = get_dict_items(dict_us)
    while(i < cells_per_user):
        try:
            if i < cells_per_user:
                print(all_list[i][1]+": ",end="")
            if all_list[i][1] == "id":
                if data_users == None:
                    if id == None:
                        input_text = "0"
                    else:
                        input_text = str(id)
                    print(input_text)
                else:
                    if id == None:
                        try:
                            input_text = str(int(data_users[-1][0])+1)
                        except IndexError:
                            input_text = str(len(data_users))
                    else:
                        input_text = str(id)
                    print(input_text)
            else:
                input_text = str(input())
            if not input_text  in ["",None] and filter_text(input_text):
                user_list[i] = input_text
                i += 1
        except (TypeError,ValueError): pass
    if data_users == None:
        return user_list
    else:
        data_users.append(user_list)
        return data_users


def merge_list_to_dict(list1):
    result = dict(zip(list_user_kir,list1))
    return result

def merge_list_to_list(list1, list2 = None):
    if list2 not in [None, "", []]:
        result = list(zip(list2, list1))
    else:
        result = list1
    return result

def merge_list_to_str(list1, list2 = None,sep="",end="\n"):
    if list2 not in [None,"",[]]:
        result = list(zip(list2, list1))
    else:
        result = list1
    text_result = ""
    for i in result:
        text_result = text_result + sep.join(i) + sep + end
    return text_result

def append_list_to_data(data,list1):
    data.append(list1)
    return data

def extend_list_to_data(data,list1):
    data.extend(list1)
    return data

def find_check_index_to_data(data,ind):
    ind = int(ind)
    for i in range(len(data)):
        if str(data[i][0]) == str(ind):
            return True, i
    return False, -1

def find_to_data(data,mode,str_search):
    # 1 - Найти по индексу
    # 2 - Найти по фамилии
    # 3 - Найти по имени
    # 4 - Найти по фамилии и имени

    for i in range(len(data)):
        if str(mode) == str(1) and str(data[i][0]) == str(str_search):
            print(str(data[i]))
            return data[i]
        elif str(mode) == str(2) and str(data[i][1]).lower() == str(str_search).lower():
            print(str(data[i]))
            return data[i]
        elif str(mode) == str(3) and str(data[i][2]).lower() == str(str_search).lower():
            print(str(data[i]))
            return data[i]
        elif str(mode) == str(4) and str(data[i][1]).lower() == str(str_search[0]).lower() and str(data[i][2]).lower() == str(str_search[1]).lower():
            print(str(data[i]))
            return data[i]
        else:
            pass

def delete_index_to_data(data,ind = None):
    while(True):
        if ind == None:
            ind = int(input_int("Введите индекс: "))
        else:
            ind = int(ind)

        is_check, ind_checked = find_check_index_to_data(data, ind)
        if is_check:
            print("   ".join(data[ind_checked]))
            print("")
            is_yes = False
            print("Удалить?\n1 - Да\n2 - Нет")
            input_delete = str(input())
            if input_delete == str(1):
                print()
                data.pop(ind_checked)

            return data
        else:
            print(f"Индекс {ind}, не существует в таблице.")
            break


def replace_index_to_data(data,ind = None):
    if ind == None:
        ind = int(input_int("Введите индекс: "))
    else:
        ind = int(ind)

    is_check, ind_checked = find_check_index_to_data(data,ind)
    if is_check:

        print("   ".join(data[ind_checked]))
        add_user = append_user(id = ind)
        data[ind_checked] = add_user
        return data
    else:
        print(f"Индекс {ind}, не существует в таблице.")



if __name__ == '__main__':
    csv_file = get_csvfile()
    bool1 = find_check_index_to_data(csv_file,1)
    replace_index_to_data(csv_file,1)
    print(csv_file)

    # result = append_user()
    # list1 = [['Фамилия','Имя','Телефон','Адрес','Описание']]
    #
    # print(append_list_to_data(list1, result))
    pass