
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



# Source https://github.com/pershinkirill/python_homework/blob/main/Seminar-3/task%235.py
#---------------------------------------------------------------

def negafibonacci_seq(n):
    fib_lst = [0, 1]
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        fib_lst.append(c)
    nega_fib = fib_lst[::-1]
    for i in range(len(nega_fib) - 1, -1, -2):
        nega_fib[i] = nega_fib[i] * (-1)
    for i in range(1, len(nega_fib)):
        nega_fib.append(fib_lst[i])
    return nega_fib

print(negafibonacci_seq(int(input())))

#---------------------------------------------------------------







# l = input("Введите низшую цену, наивысшую цену, через пробел: \n")
# a,b = map(float,l.split())
# perc = [0,.236,.382,.50,.618,1]
# diff = b-a
# for x in perc:
#     print("{}%\t|\t{}\t|\t{}\t|".format(x*100,a+diff*x,b-diff*x))




# def fib(n):
#     if n in (1, 2):
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(5))



# def fib(n: int) -> list:
#     if n == 1:
#         return [1]
#     elif n == 2:
#         return [1, 1]
#
#     li = fib(n-1)
#     li.append(li[-1] + li[-2])
#     return li
#
# print(fib(15))