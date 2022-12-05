
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.(Вывод тех элементов, которые были без повторов)
#
# Ввод: 1 2 3 2 4 4
#
# Вывод: 1 3

from random import randint
arrayList = [str(randint(1,5)+i) for i in range(6)]

dictDubl = {}
for i in arrayList:
    if dictDubl is not i:
        try:
            dictDubl[i] = dictDubl[i] + 1
        except:
            dictDubl[i] = 1
print(dictDubl)
print(f'Ввод: {", ".join(arrayList)}')
resultList = []
for n in dictDubl:
    if dictDubl.get(n) == 1: resultList.append(str(n))
joinResultList = ", ".join(resultList)
print(f'Вывод: {joinResultList if len(resultList) > 0 else "Отсутствуют, не дублированные числа"}')
