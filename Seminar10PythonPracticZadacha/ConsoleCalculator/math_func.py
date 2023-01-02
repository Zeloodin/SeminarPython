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

sqrt = lambda n,p=2:n ** (1/p)
pow = lambda n,p=2: n ** p
mod = lambda n,p: n % p

# 2.0 version
def op_num_sign(sgn,first,second=None):
    try:
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
    except OverflowError:
        print("Результат слишком большой")
        return None
    except ValueError:
        print("Не удалось преобразовать строку в число с плавающей запятой")
        return None
    except ZeroDivisionError:
        print("Деление числа на ноль")
        return None

# 1.0 version
def number_operation(left_n,right_n,operat):
    try:
        match operat:
            case "^":
                return float(left_n)**float(right_n)
            case "*":
                return float(left_n)*float(right_n)
            case "/":
                return float(left_n)/float(right_n)
            case "+":
                return float(left_n)+float(right_n)
            case "-":
                return float(left_n)-float(right_n)
            case _:
                return ""
    except OverflowError:
        print("Результат слишком большой")
        return ''
    except ValueError:
        print("Не удалось преобразовать строку в число с плавающей запятой")
        return ''
    except ZeroDivisionError:
        print("Деление числа на ноль")
        return ''