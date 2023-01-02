#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math_func as mathf
import string_func as strf

# The order of operations
# PEMDAS
# parentheses, exponents, multiplication, division, addition, subtraction

# Ex. Use the order of operations to simplify the expression 3×4^2+8−(11+4)^2÷3.
#
# Parentheses: 3×4^2+8−(15)^2÷3
# Exponents: 3×16+8−225÷3
# Multiplication/Division: 48+8−75
# Addition/Subtraction: −19

# Parentheses: 3*4^2+8-(15)^2/3
# Exponents: 3*16+8-225/3
# Multiplication/Division: 48+8-75
# Addition/Subtraction: -19

def text_to_rule_math(text):
    text = text.replace("×","*").replace("÷","/").replace(":","/").replace("−","-")
    if strf.check_math_rules(text):
        res = strf.split_string_to_math(text)
        res2 = strf.simplify_text_for_math(res)
        return res2
    else:
        print(f"Не может обрабатываться: {text}")
        # res = strf.split_string_to_math(text)
        # res2 = strf.simplify_text_for_math(res)
        # return res2


if __name__ == '__main__':
    text = "3*4^2+8-(11+4)^2/31/0"

    print(text_to_rule_math(text))

