#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math_func

def split_string_to_math(text):
    symbols = "+-*/^:()"
    nums = "0123456789"
    point = "."
    text = text.replace(" ","")
    for i in range(len(text)-1,0,-1):
        try:
            if (text[i-1] in nums and text[i] == "." and text[i+1] in nums):
                text = text[:i - 1] + " " + text[i-1:i+2] + " " + text[i + 2:]

            elif (text[i] in nums and text[i+1] == "." and text[i+2] in nums):
                i = i + 1
                text = text[:i - 1] + " " + text[i - 1:i + 2] + " " + text[i + 2:]

            elif (text[i-2] in nums and text[i-1] == "." and text[i] in nums):
                i = i - 1
                text = text[:i - 1] + " " + text[i-1:i+2] + " " + text[i + 2:]

            elif text[0] in symbols:
                text = text[:i] + " " + text[i] + text[i + 1:]

            elif text[-1] in symbols:
                text = text[:i] + text[i] + " " + text[i + 1:]

            elif text[i] in symbols and text[i+1] in symbols and text[i-1] in symbols:
                text = text[:i] + text[i] + " " + text[i + 1:]

            elif text[i] in symbols and text[i+1] in symbols:
                text = text[:i] + " " + text[i] + " " + text[i + 1:]

            elif text[i] in symbols and text[i - 1] in symbols:
                text = text[:i] + text[i] + " " + text[i + 1:]

            elif text[i] in symbols:
                text = text[:i] + " " + text[i] + " " + text[i + 1:]

        except IndexError: pass
    split_text = text.split(" ")
    try:
        for i in range(len(split_text)-1,0,-1):
            if str(split_text[i]) == "":
                split_text.pop(i)
    except IndexError:
        pass
    return split_text

def check_math_rules(text):
    symbols = "+-*/^:."
    brackets = "("
    symbol = 0
    check_count_brackets = count_brackets(text)
    if not check_count_brackets[2]:
        print(f"Колличество открытых и закрытых скобок. (:{check_count_brackets[0]}, ):{check_count_brackets[1]}")
        return False

    for i in range(len(text)-1):
        if (text[i-1] in brackets and text[i] in symbols) and text[i] != "-":
            return False
        elif (text[0] in symbols or text[-1] in symbols) and text[0] != "-" :
            return False
        elif text[symbol] != text[i] and text[i] in symbols:
            symbol = i
        elif text[symbol] == text[i] and text[i] in symbols and symbol != i and abs(i - symbol) == 1:
            return False
    return True

def count_brackets(text):
    left_brackets = 0
    right_brackets = 0
    for i in range(len(text)):
        if text[i] == "(": left_brackets += 1
        elif text[i] == ")": right_brackets += 1
    if left_brackets == right_brackets != 0:
        return [left_brackets, right_brackets, True, True]
    elif (left_brackets  == right_brackets) != 0:
        return [left_brackets, right_brackets, True, False]
    else:
        return [left_brackets, right_brackets, False, True]

def simplify_text_for_math(split_text):

    symbols = "+-*/^()"
    # symbols = "+-*/^:."
    nums = "0123456789."
    brackets = "("
    minus = "-"
    i = 0
    print(split_text)
    while(i < len(split_text)-1):
        if math_func.is_num(split_text[i]):
            if type(split_text[i]) in [int,float]: i += 1
            print(split_text[i-1:i+1],split_text[i],math_func.is_num(split_text[i]),i)
            split_text[i] = float(split_text[i])
            if str(split_text[i-1]) == minus and not (str(split_text[i-2]) in nums or math_func.is_num(split_text[i-2]) or str(split_text[i-2]) in brackets):
                split_text[i] = -split_text[i]
                split_text.pop(i-1)
                print(split_text[i-1],split_text[i-2])
        else:
            i += 1
        # print(f"{split_text[:i]}  ||__type:__ {type(split_text[i])} value:__ {split_text[i]} __||  {split_text[i + 1:]},{i},{len(split_text)},{split_text[i]}")



if __name__ == '__main__':
    print("Запуск бота")
    text = "-1+(4+(6+(1-2.5-2)*(6/3)))"
    text1 = "(-(2+5))"
    text2 = "(-1-(-(2+5)))"

    text_split = [i for i in [text,text1,text2]]

    for i in text_split:

        res2 = count_brackets(i)
        res1 = check_math_rules(i)
        res = split_string_to_math(i)

        res3 = simplify_text_for_math(res)
        # res4 = s

        print(res, res1, res2, res3,sep="\n")
        print(end="\n"*1)

