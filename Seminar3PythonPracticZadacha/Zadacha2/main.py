# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#Пример:
#
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math
from math import floor


def IsEvenList(arrayList):
    if (int((len(arrayList)/2) * 100) % 100) != 0 :
        return 1+int(len(arrayList)/2)
    else:
        return int(len(arrayList)/2)

def isNoneList(listNums):
    isNone = True
    count = 2
    while(count > 0):
        count -= 1
        try:
            for indx in range(len(listNums)):
                if listNums[indx] is None :
                    del listNums[indx]
                else:
                    isNone = False
        except IndexError: pass
    if isNone: listNums = [0]
    return listNums


def RunCode(listNums):
    listNums = isNoneList(listNums)
    saveListNums = listNums.copy()
    resultList = []
    for i in range(IsEvenList(listNums)):
        if len(listNums) != 1:
            resultList.append(round(listNums[0]*listNums[-1],2))
            del listNums[0]
            del listNums[-1]
        else:
            resultList.append(round(listNums[0] * listNums[-1],2))
            del listNums[0]
    print(saveListNums,"=>",resultList)

array2dListNumbers = [[2, 3, 4, 5, 6],
                      [2, 3, 5, 6],
                      [12, 15, 16],
                      [12, 15],
                      [12, 2, 15, 3, 16, 4, 12, 5, 15, 6, 192, 2, 225, 3, 180, 5, 15, 6, 12, 12, 15, 16],
                      [i*i if i*i%2 == 0 else None for i in range(1,11,1)],
                      [int(i**j) for j in range(2,6) for i in range(2,6)],
                      [int(j**i) for j in range(2,6) for i in range(2,6)]]

for allList in array2dListNumbers:
    RunCode(allList)

