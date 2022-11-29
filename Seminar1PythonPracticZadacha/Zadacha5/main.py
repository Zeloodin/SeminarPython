import math
# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def what_coordinate(coordinate): # Координаты X=1 Y=2 Z=3 4......N
    match(coordinate):
        case 0:
            pass
        case 1:
            return "X"
        case 2:
            return "Y"
        case 3:
            return "Z"
        case _:
            return coordinate


points, coorNum = 2, 2
coordinates = [[0 for j in range(coorNum)] for i in range(points)]

for k in range(points):
    if k == 0: txt = "Точка A"
    else:  txt = "Точка B"
    print(txt)
    for m in range(coorNum):
        print(f"Введите значение {what_coordinate(m+1)} координаты: ",end="")
        # print(end="\r")
        try:
            coordinates[k][m] = float(input())
        except:
            coordinates[k][m] = 0
print(coordinates)

print("\n"*2,end="")

for i in range(len(coordinates)):
    print(f"Point{i + 1}",end=" ")
    for j in range(len(coordinates[i])):
        print(f"{what_coordinate(j)}:{coordinates[i][j]}",end=" ")
    print()

listResult = [0 for i in range(len(coordinates[0]))]

for n in range(len(listResult)):
    listResult[n] = coordinates[1][n] - coordinates[0][n]

def PrintResult(result):
    print(f"Расстояние между Ponit1 и Point2: {sqrt_PowX2_PowY2_PowZ2}")

match(coorNum):
    case 0:
        pass
    case 1:
        sqrt_PowX2_PowY2_PowZ2 = float(str(round(math.sqrt(math.pow(listResult[0],2)), 3))[:-1])
        PrintResult(sqrt_PowX2_PowY2_PowZ2)
    case 2:
        sqrt_PowX2_PowY2_PowZ2 = float(str(round(math.sqrt(math.pow(listResult[0],2) + math.pow(listResult[1], 2)), 3))[:-1])
        PrintResult(sqrt_PowX2_PowY2_PowZ2)
    case 3:
        sqrt_PowX2_PowY2_PowZ2 = float(str(round(math.sqrt(math.pow(listResult[0], 2) + math.pow(listResult[1], 2) + math.pow(listResult[2], 2)), 3))[:-1])
        PrintResult(sqrt_PowX2_PowY2_PowZ2)
    case _:
        pass

