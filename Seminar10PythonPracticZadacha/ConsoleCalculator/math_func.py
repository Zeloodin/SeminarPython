#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_num(n):
    is_num_real = list("0123456789.")
    for i in list(str(n)):
        if not i in is_num_real:
            return False
    return True

def is_num_real(n):
    is_num_real = list("0123456789.")
    for i in list(str(n)):
        if not i in is_num_real:
            return False
    return True

def is_num_int(n):
    is_num_int = list("0123456789")
    for i in list(str(n)):
        if not i in is_num_int:
            return False
    return True

def str_to_num(indx):
    print("ssssssssssssss")




sqrt = lambda n,p=2:n ** (1/p)
pow = lambda n,p=2: n ** p
mod = lambda n,p: n % p

def sign(sgn,first,second=None):
    if second != None:
        match sgn:
            case "+":
                return first+second
            case "-":
                return first-second
            case "*":
                return first*second
            case "/":
                return first/second
            case "^":
                return first ** second
            case "√":
                return first ** (1/second)
            case "%":
                return first % second
            case _:
                pass
    else:
        match sgn:
            case "+":
                return first
            case "-":
                return -first
            case "√":
                return first ** 0.5