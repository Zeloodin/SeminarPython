
def filter_text(text):
    for i in range(len(text)-1):
        if text[i] == ";" or text[i] == "n" and text[i+1] == "\\":
            return False
    return True

def prime_mode(n):
    if n.isdigit() and n in ["0","1","2","3","4","5","6","7","8","9"]:
        return True
    else:
        return False

def selected_mode(n,mode):
    if n.isdigit() and mode == 0:  # 1 - создать новый телефонный справочник
        return True

    elif n.isdigit() and n in ["1","2"] and mode == 1: # 1 - создать новый телефонный справочник
        return True

    elif n.isdigit() and n in ["1","2"] and mode == 2: # 2 - добавить в телефонный справочник
        return True

    elif n.isdigit() and n in ["1","2","3","4","5"] and mode == 3: # 3 - найти в справочнике
        return True

    elif n.isdigit() and n in ["1","2"] and mode == 4: # 4 - заменить в справочнике
        return True

    elif n.isdigit() and n in ["1","2"] and mode == 5: # 5 - удалить из телефонного справочника
        return True

    elif n.isdigit() and n in ["1","2","3"] and mode == 6: # 6 - импорт справочника
        return True

    else:
        return False
