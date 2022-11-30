# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
#Пример:
#
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

arrayListNumber = [randint(0,10) for i in range(5)]
arraySplitSum = [arrayListNumber[i] for  i in range(len(arrayListNumber)) if i % 2 == 1]
arraySplitSumStr = [str(arraySplitSum[i]) for i in range(len(arraySplitSum))]
print(arrayListNumber," -> на нечётных позициях элементы ", " и ".join(arraySplitSumStr),", ответ: ",sum(arraySplitSum),sep="")