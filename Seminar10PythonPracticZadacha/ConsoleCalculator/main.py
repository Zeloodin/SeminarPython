#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math_func as mathf
import string_func as strf
import math_expr_func as mathexf
import calc_core_06 as care





if __name__ == '__main__':
    text = "3*4^2+8-(15)^2/3"
    text_math = mathexf.text_to_rule_math(text)
    calc_result = care.CalcRun(text)
    print(text_math,calc_result)
