#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math_func as mathf
import string_func as strf
import math_expr_func as mathexf
import calc_core_06 as care
import math_brackets_func as mathbraf



# text_math = mathexf.text_to_rule_math(text)
def algorithm_of_mathematical_expressions(text_math):
    symbols = "+-*/^()"
    nums = "0123456789."
    brackets = ["(",")"]
    bracket_open = "("
    bracket_close = ")"

    len_text = len(text_math)
    min_ind = 0
    max_ind = len(text_math)
    i_ind = min_ind

    mathbraf.count_level_brackets(text_math)




if __name__ == '__main__':
    text = "3*4^2+8-(15)^2/3))"
    text_math = mathexf.text_to_rule_math(text)

    print(mathbraf.check_count_matching_brackets(text_math,is_check=True))

    print(mathbraf.count_level_brackets(text_math))

    print(algorithm_of_mathematical_expressions(text_math))

    # print(text_math)
    # alg_of_math_exp = algorithm_of_mathematical_expressions(text_math)
    # print(alg_of_math_exp)
