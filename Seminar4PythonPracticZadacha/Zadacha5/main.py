# Polynomial
#
# 5. Дополнительное Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
#
# Файл1: 2*x^2 + 4*x + 5
#
# Файл2: 41*x^3 + 6*x^2 + 2*x + 98
#
# Вывод Файл3: 41*x^3 + 8*x^2 + 6*x + 103


# textFile = open(f"File1.txt", "r")
# textFile.read().replace("^","**")
# textFile.close()
#
# textFile = open(f"File2.txt", "r")
# textFile.read().replace("^","**")
# textFile.close()

# Комментарий: Был взят из сайта github.com, этот код.
# Source
# https://github.com/NataSola/HW2_Python/blob/main/34_Sum_polynom.py

import re
import itertools


file1 = 'File1.txt'
file2 = 'File2.txt'
file_sum = 'File3Sum.txt'

# Получение данных из файла

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)



# https://www.cyberforum.ru/python/thread1972755.html

# with open('input01.txt') as f_i, open('output01.txt', 'w') as f_o:
#     equation, x = f_i.read().split('\n')
#     f_o.write(str(eval(equation.replace('x', x))))

# eval(equation, {'x':x})