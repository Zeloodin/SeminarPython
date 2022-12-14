from string_func import prime_mode, selected_mode
from generator_list import gen_list

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

def input_selected_number(mode_num=0):
    while (True and mode_num != 0):
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


def read_list(list1,sep=" ", end="\n", show = True):
    text = ""
    for i in range(len(list1)):
        if show:
            print(list1[i],sep=sep,end=end)
        text = text + (sep if i != 0 else "") + list1[i]
    text = text + end
    return text


if __name__ == '__main__':
    list1 = [gen_list()]
    list1[0] = "Sad"
    list1[1] = "Mercury"
    list1[2] = "12321-4124"
    list1[3] = "Moscow"
    list1[4] = "Eath"
    print(list1)
    print(read_list(list1, sep="  ||  ", end="\n", show=False))