#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_count_matching_brackets(text_math,is_check = False):
    global brackets_present
    if text_math == None: return None
    len_text = len(text_math)
    bracket_open = "("
    bracket_close = ")"

    def lambda_bra_pre(ind,n):
        global brackets_present
        brackets_present[ind] += n

    is_brackets_present = False
    brackets_present = [0,0]
    [(lambda_bra_pre(0, 1)) if (text_math[i] == bracket_open) else
     (lambda_bra_pre(1, 1)) if (text_math[i] == bracket_close) else 0
     for i in range(len_text)]

    matching_brackets = sum([(-brackets_present[i] if i == 0 else
                               brackets_present[i] if i == 1 else None)
                             for i in range(len(brackets_present))])

    if is_check:
        lrbrackets = ["открытая ( скобка","закрытая ) скобка"]
        bool_brackets = True
        if matching_brackets < 0:
            temp_string = lrbrackets[0]
            lrbrackets[0] = lrbrackets[1]
            lrbrackets[1] = temp_string
        elif matching_brackets > 0:
            pass
        else:
            bool_brackets = False

        if bool_brackets:
            print(f"Отсутствует {lrbrackets[0]}, или присутствует лишняя {lrbrackets[1]}")
            print(f"Колличество открытых скобок ( :{brackets_present[0]}")
            print(f"Колличество закрытых скобок ) :{brackets_present[1]}")

    if brackets_present[0] > 0 or brackets_present[1] > 0:
        is_brackets_present = True

    return [is_brackets_present,matching_brackets,brackets_present[0],brackets_present[1]]

def count_level_brackets(text_math):
    if text_math == None: return None
    brackets = list("()")
    bracket_open = "("
    bracket_close = ")"
    len_text = len(text_math)
    i_brackets_level = 0
    max_brackets_level = 0
    min_brackets_level = 0
    count_brackets_open = 0
    count_brackets_close = 0

    if check_count_matching_brackets(text_math=text_math)[0]:
        for i in range(len_text):
            if text_math[i] == bracket_open:
                i_brackets_level += 1
                count_brackets_open += 1
                if i_brackets_level > max_brackets_level:
                    max_brackets_level = i_brackets_level
            elif text_math[i] == bracket_close:
                i_brackets_level -= 1
                count_brackets_close += 1

            if i_brackets_level < 0:
                min_brackets_level += 1

    if min_brackets_level > 0:
        print("Ошибка. В тексте закрытые скобки находятся первее чем открытые скобки.\nПример: )2-6(*2\n)3-2(-1\n")

    return [max_brackets_level,min_brackets_level,count_brackets_open+count_brackets_close,count_brackets_open,count_brackets_close,count_brackets_close-count_brackets_open]