
# sign_in login sessions
# sign_up register registrations
data_base_ilp = [[2,1,"логин","пароль","Клещева","Валентина"],[3,2,"ученик1а","какойпароль?","Кувшинов","Рашит"],[4,2,"1","1","Безус","Рэм"]]

def sign_in():
    user_login_password = ["",""]
    print_log_pas = ["Введите логин:","Введите пароль:"]
    print_log_pas_error = ["Такого логина нет.","Ввели неправильный пароль"]
    is_true = False
    n = 0
    # while(not is_true):
    #     is_error = False
    #     print(print_log_pas[n],end="")
    #     user_login_password[n] = str(input())
    #     for logpas in data_base_ilp:
    #         if user_login_password[n].lower() == logpas[2+n].lower():
    #             if n == 1:
    #                 is_true = True
    #             break
    #     else:
    #         print(print_log_pas_error[n])
    #         is_error = True
    #     if not is_error:
    #         n += 1
    user_login_password = ["логин", "пароль"]

    return user_login_password








