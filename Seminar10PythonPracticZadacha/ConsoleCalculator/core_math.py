#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math_func as mathf
import string_func as strf
import math_expr_func as mathexf
import calc_core_06 as care
import math_brackets_func as mathbraf

# The order of operations
# PEMDAS
# parentheses, exponents, multiplication, division, addition, subtraction

# Ex. Use the order of operations to simplify the expression 3*4*2+8-(11+4)^2/3.
# Parentheses: 3*4^2+8-(15)^2/3
# Exponents: 3*16+8-225/3
# Multiplication/Division: 48+8-75
# Addition/Subtraction: -19





def op_math_to_text(text_math):
    result = text_math.copy()
    signs = list("^*/+-")
    for sign in signs:
        while (sign in result):
            ni = 0
            while (ni < len(result)):
                if sign == result[ni]:
                    bracket_string_result = mathf.op_num_sign(result[ni], result[ni - 1], result[ni + 1])
                    result.pop(ni)
                    result.pop(ni)
                    result[ni - 1] = bracket_string_result
                ni += 1

    return result



def op_in_brackets(text_math):
    max_brackets_level = mathbraf.count_level_brackets(text_math)[0]
    bracket_open = "("
    bracket_close = ")"
    while (max_brackets_level > 0):
        len_text = len(text_math)
        i = 0
        if i >= len_text: break

        ind_open = 0
        ind_close = 0

        level_brackets = 0

        is_find_max_open = False
        is_find_max_close = False

        while (i < len_text):
            if text_math[i] == bracket_open:
                level_brackets += 1
            elif text_math[i] == bracket_close:
                level_brackets -= 1

            if level_brackets == max_brackets_level and not is_find_max_open:
                ind_open = i
                is_find_max_open = True
            elif is_find_max_open and text_math[i] == bracket_close and not is_find_max_close:
                ind_close = i
                is_find_max_close = True
            i += 1

        if is_find_max_open and is_find_max_close:
            text_in_brackets = text_math[ind_open + 1:ind_close]
            result_num = op_math_to_text(text_in_brackets)
            text_math = text_math[:ind_open] + result_num + text_math[ind_close + 1:]

        max_brackets_level = mathbraf.count_level_brackets(text_math)[0]

    return text_math



def action_expr_math(text_math):
    max_brackets_level = mathbraf.count_level_brackets(text_math)[0]
    if max_brackets_level > 0:
        text_math = op_in_brackets(text_math)
    result_num = op_math_to_text(text_math)
    return result_num




# text_math = mathexf.text_to_rule_math(text)
def algorithm_of_mathematical_expressions(text_math):
    if text_math != None:
        # symbols = "+-*/^()"
        # nums = "0123456789."
        # brackets = ["(",")"]
        # bracket_open = "("
        # bracket_close = ")"
        #
        # len_text = len(text_math)
        # min_ind = 0
        # max_ind = len(text_math)
        # i_ind = min_ind

        max_brackets_level,min_brackets_level,sum_brackets,count_brackets_open,count_brackets_close,difference_brackets = mathbraf.count_level_brackets(text_math)
        if difference_brackets == 0 and min_brackets_level == 0 and count_brackets_open == count_brackets_close:
            result = action_expr_math(text_math)
        else:
            if difference_brackets != 0:
                print("Присутсвуют не парные скобки")
            if min_brackets_level > 0:
                print("Присутсвуют закрытые скобки перед открытыми скобками.\nПример: )2+2(")
        return result






if __name__ == '__main__':
    text = "3*4^2+8-((4+11-20)/2)^2/3"
    text_math = mathexf.text_to_rule_math(text)

    # print(mathbraf.check_count_matching_brackets(text_math,is_check=True))
    #
    # print(mathbraf.count_level_brackets(text_math))

    print(algorithm_of_mathematical_expressions(text_math))

    # print(text_math)
    # alg_of_math_exp = algorithm_of_mathematical_expressions(text_math)
    # print(alg_of_math_exp)
