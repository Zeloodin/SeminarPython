
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#
# 24
#
# 2 2 2 3

import lib

textFile = open(f"listPrimeNumber.txt", "r")
listPrimeNumber = textFile.read().split("\n")

for i in range(len(listPrimeNumber)):
    try:
        listPrimeNumber[i] = int(listPrimeNumber[i])
    except ValueError: pass


numberInit = 1000000000000
print(numberInit)

numDecIntPriNum = [] # Number decomposed into prime numbers

indexPrime = 0
numInt = numberInit
countIter = 0
while(True):

    if numInt == 1:
        break

    if lib.IsIntegerNumber(numInt / listPrimeNumber[indexPrime]):
        numDecIntPriNum.append(listPrimeNumber[indexPrime])
        numInt /= listPrimeNumber[indexPrime]
        indexPrime = 0
    else:
        indexPrime += 1

print(numDecIntPriNum)


# Не знаем где ошибка. (while n/j == n//j:) Она есть, но как решить её???
# n = 1234
# j = 2
# while(True):
#     print(n/j)
#     while n/j == n//j:
#         n = n/j
#         print(j,"*",end=" ")
#         if n == 1: break
#     else:
#         if j <= n/j:
#             j = j + 1
#         else:
#             break
