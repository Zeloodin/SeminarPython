
list_user_kir = ['id','Фамилия','Имя','Телефон','Адрес','Описание']
list_user = ['id',"Surname","Name","Phone","Address","Description"]
list_print_user = ['id',"Введите Фамилию","Введите Имя","Введите Номер телефона","Введите Адрес","Введите Описание"]
dict_us = dict(zip(list_user,list_print_user))
cells_per_user = len(dict_us) # number_of_cells_per_user

if __name__ == '__main__':
    print(cells_per_user)
    print(list_user)
    print(list_print_user)
    print(dict_us)