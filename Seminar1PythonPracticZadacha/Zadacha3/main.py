# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Если у точки обе координаты (x и y) положительны, то она принадлежит первой четверти.
# Если координата x отрицательна, а y положительна, то точка находится во второй четверти.
# Если обе координаты отрицательны, то точка принадлежит третьей координатной четверти.
# Если x положительна, а y отрицательна, то точка находится в IV четверти.

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

def inputFloat(str = ""):
    print(str,end=" ")
    while(True):
        try:
            strN = float(input().replace(",","."))
            break
        except:
            print(str, end=" ")
    return strN

xy = inputFloat("X = "), inputFloat("Y = ")

result = Coor4(xy)
print(result)