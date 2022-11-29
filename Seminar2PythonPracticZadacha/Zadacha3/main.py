# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
#
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
#
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


import random
lenList = 4
countIndx = 5

randomIndex = [2, 2, 3, 1, 8] # [random.randint(0,2*lenList) for i in range(countIndx)]
print(f"randomIndex={randomIndex}")
arrayNumber = [i for i in range(-lenList,lenList+1)]
print(f"arrayNumber={arrayNumber}")
indexList = randomIndex
saveIndexList = []
for i in range(len(indexList)):
    # print(f"Длина: {len(arrayNumber)}. Индекс: {i}. Значение: {indexList[i]}")
    if len(arrayNumber) < indexList[i]:
        print("Вышли за границу длины границу диапазона списка, индекс пропускается")
        continue
    saveIndexList.append(arrayNumber[indexList[i]])
print(f"saveIndexList={saveIndexList}")

def SumProduct(array,sp=False):
    if sp == False: number = 0
    elif sp == True: number = 1
    else: number = 0

    for i in range(len(array)):
        if saveIndexList[i] != 0:
            if sp == False : number += saveIndexList[i]
            elif sp == True: number *= saveIndexList[i]
            else: pass

    return number

print(f"{SumProduct(saveIndexList)}")
print(f"{SumProduct(saveIndexList,True)}")
