from generator_list import gen_list
from constant import cells_per_user, dict_us, list_user, list_user_kir
from console_func import inp_str, out_str
from string_func import filter_text

def get_dict_keys(dict):
    return [n for n in dict.keys()]

def get_dict_values(dict):
    return [n for n in dict.values()]

def get_dict_items(dict):
    return [n for n in dict.items()]

def append_user(data_users = None):
    user_list = gen_list()
    i = 0
    all_list = get_dict_items(dict_us)
    while(i < cells_per_user):
        try:
            if i < cells_per_user:
                print(all_list[i][1]+": ",end="")
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



if __name__ == '__main__':
    result = append_user()
    list1 = [['Фамилия','Имя','Телефон','Адрес','Описание']]

    print(append_list_to_data(list1, result))