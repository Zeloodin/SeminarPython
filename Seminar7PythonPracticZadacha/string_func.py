from generator_list import gen_list
from constant import cells_per_user
from console_func import inp_str

def filter_text(text):
    for i in range(len(text)-1):
        if text[i] == ";" or text[i] == "n" and text[i+1] == "\\":
            return False
    return True

def prime_mode(n):
    if n.isdigit():
        return True
    else:
        return False