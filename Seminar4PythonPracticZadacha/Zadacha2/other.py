# https://github.com/RomanMenshikov92/GB_lesson-Python-/blob/0e47ef83e3b56910a6c80a3e36b942ac8ac6d0ec/homework-4/hw__4.2.py

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls||clear')

print('Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.\n')


n = int(input("Введите число n: "))
i = 2
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f'\nСписок простых множителей {list} от числа {n}\n')



# https://github.com/Vjacheslav666/Seminar_DZ_Python/blob/542c147af8eb0e67adf23a9cba9ce9cccea09b85/Seminar_4_Python/Task2.py

# Задайте натуральное число N.
# Напишите программу, которая составит список простых
# множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")


# https://github.com/OlgaTiurina/HW4_Python_prog/blob/3393bd8ea8159820b938e6495d757617ee7fe195/ex2.py

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")



# https://github.com/SilverXuz/python_DZ_4/blob/3b8fa1bd9497b5d5a0e8212c4ec6df33b1bc1e4f/Task2/Task2.py

"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

N = int(input('Задайте натуральное число: '))
result = []
p = 2

while p != N:
    if N % p == 0:
        N /= p
        result.append(p)
    else:
        p += 1
else:
    result.append(p)
print(result)

# 2
# n = int(input('Введите натуральное число: '))
# if n > 0:
#     multipliers = []
#     while n > 1:
#         for i in range(2, n + 1):
#             count = True
#             for j in range(2, i):
#                 if i % j == 0:
#                     count = False
#                     break
#             if count:
#                 while n % i == 0:
#                     multipliers.append(i)
#                     n /= i
#     print(multipliers)
# else:
#     print('Введено не натуральное число')


# Виталий
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число N = '))
# prime_number = 2
# list_factor = []

# while prime_number != n:
#     if n % prime_number == 0:
#         n /= prime_number
#         list_factor.append(prime_number)
#     else:
#         prime_number += 1
# #if n == prime_number:
# else:
#      list_factor.append(prime_number)

# print(list_factor)



# https://github.com/OlgaTiurina/HWork4_Python/blob/c664ef62a4e3a922d9aacc508f56ab6898ccfabd/ex2.py

# Задайте натуральное число N.
# Напишите программу, которая составит список простых
# множителей числа N.
# N = 6 | N = 12 | 32 | 13 | 9 | 18 | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

print("Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

num = int(input("Введите число: "))
i = 2 # первое простое число
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")


# https://github.com/ooo-kupina/homeworks_Python/blob/4ae08d677f07e24462ec1f774eff3dc827a805b5/hw_4_Python/Task_2_hw_4.py

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

print("Данная программа составит список простых множителей числа N,\n\
которое задаёт пользователь.")
number = int(input('Введитe натуральное число N: '))
N = number
multipliers = []
for i in range(2, int(number ** 0.5) + 2):
    while number % i == 0:
        multipliers.append(i)
        number //= i
if number != 1:
    multipliers.append(number)
print(f"Список простых множителей числа {N}: {multipliers}")


# https://github.com/RomanBelykh/PythonHW/blob/5f9521f2bd9cd71b640870217438792dff1eefbd/HW4.py/Task2.py

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('Чтобы составит список простых множителей натурального числа N, введите это число! ')
n = int(input("Введите число N: "))
numbers = []
a = 2
m = n
while a * a <= n:
        if n % a == 0:
            numbers.append(a)
            n//=a
        else:
            a += 1
numbers.append(n)
print(f'Cписок простых множителей числа {m} = {numbers}')



# https://github.com/ignatKupryashin/GB_Python_HW04/blob/76196fc3187866e0a95eb02fe57eb6842a44c426/Task2.py

# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# *Пример*
#
# - при N=236     ->        [2, 2, 59]

# from common_methods import title

# Метод красивого вывода заголовков
def title(title_string):
    print("\n" + title_string + "\n")


title("2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.")

question = int(input("Введите число N: "))
answer = []
while question > 1:
    for i in range(2, question + 1):
        if question % i == 0:
            answer.append(i)
            question = int(question / i)
            break
print(answer)





# https://github.com/YuliaEgorova88/-Python/blob/f173a6d8e0ac2106f58683faa2c46715e8357639/Homework1/task2.py

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

list = []
number = int(input("Введите число N: "))
for n in range(2, number):
    if number % n == 0:
        list.append(n)

print(list)

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factorization(n):
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(n)
    return primfac


number = int(input('Inpunt number: '))
print(f'{factorization(number)}')





# https://github.com/STyutvin/Seminar-04-hw-/blob/8fc217e6e285094eddd4b5ca3529e43591c14419/Seminar%2003(hw).py

# Задача №1. Вычислить число c заданной точностью d.
# from math import pi
# d =  int(input('Введите число для заданной точности числа Пи: '))
# print(f'Число Пи с заданной точностью {d} равно {round(pi, d)}')
#-------------------------------------------------

# Задача №2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# n=int(input('Введите число N: '))
# empty_list=[]
# for i in range(0,n-1):
#     if n%(n-i)==0:
#         empty_list.append((int(n/(n-i))))
# print(f'Список простых множителей для числа N={n}: {empty_list}')
#-------------------------------------------------

# Задача №3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# from random import randint
# some_list = []
# i = 1
# n = int(input('Введите количество элементов в списке: '))
# for i in range(n):
#     some_list.append(randint(1,5))
#     i += 1
# print(f'Ваш случайно сгенерированный список из {n} элементов: {some_list}')
# unique_list=list(set(some_list))
# print(f'Список уникальных элементов {unique_list}')
#-------------------------------------------------



