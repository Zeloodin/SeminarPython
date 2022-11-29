# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Если у точки обе координаты (x и y) положительны, то она принадлежит первой четверти.
# Если координата x отрицательна, а y положительна, то точка находится во второй четверти.
# Если обе координаты отрицательны, то точка принадлежит третьей координатной четверти.
# Если x положительна, а y отрицательна, то точка находится в IV четверти.

import random

def GenRandRange(corN):
    if corN == 1:
        return [round(random.randint(1, 100)/100, 3),round(random.randint(1, 100)/100, 3)]
    elif corN == 2:
        return [-round(random.randint(1, 100)/100, 3),round(random.randint(1, 100)/100, 3)]
    elif corN == 3:
        return  [-round(random.randint(1, 100)/100, 3),-round(random.randint(1, 100)/100, 3)]
    elif corN == 4:
        return  [round(random.randint(1, 100)/100, 3),-round(random.randint(1, 100)/100, 3)]
    else:
        pass

def RandArrayNumber(corN):
    return [GenRandRange(corN) for i in range(10)]

def GeneratorRandomPoint(corN):
    if corN == 1: listRandom = RandArrayNumber(corN)
    elif corN == 2: listRandom = RandArrayNumber(corN)
    elif corN == 3: listRandom = RandArrayNumber(corN)
    elif corN == 4: listRandom = RandArrayNumber(corN)
    else: listRandom = 0
    for i in range(len(listRandom)):
        print(listRandom[i])

def Coor4(numb):
    if numb[0] > 0 and numb[1] > 0:
        return 1
    elif numb[0] < 0 and numb[1] > 0:
        return 2
    elif numb[0] < 0 and numb[1] < 0:
        return 3
    elif numb[0] > 0 and numb[1] < 0:
        return 4
    elif numb[0] == 0 or numb[1] == 0:
        pass #return 0
    else:
        pass

def CoorFind4(n):
    if n == 1:
        GeneratorRandomPoint(n)
        return "x > 0 and y > 0"
    elif n == 2:
        GeneratorRandomPoint(n)
        return "x < 0 and y > 0"
    elif n == 3:
        GeneratorRandomPoint(n)
        return "x < 0 and y < 0"
    elif n == 4:
        GeneratorRandomPoint(n)
        return "x > 0 and y < 0"
    else:
        pass


def inputFloat(str = ""):
    print(str,end=" ")
    while(True):
        try:
            strN = float(input().replace(",","."))
            break
        except:
            print(str, end=" ")
    return strN

# xy = inputFloat("X = "), inputFloat("Y = ")
# result = Coor4(xy)
# print(result)

print(CoorFind4(inputFloat("Nomer 1/4: ")))