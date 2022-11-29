# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import random

def runFactorial(num):
    initN = 1
    for i in range(num,0,-1):
        initN *= i
    return initN



def runCode(modeNumber):
    print(f"Запуск кода. Выбранный режим {modeNumber}.")
    numN = 0
    if modeNumber == "1":
        trueFalse1 = True
        while(trueFalse1):
            trueFalse1 = False
            try:
                numN = int(input("Введите целое число: "))
            except:
                print("Введённое в строку, не было целым числом.")
                trueFalse1 = True
        return numN
    elif modeNumber in ["2","3"]:
        trueFalse2 = True
        while(trueFalse2):
            trueFalse2 = False
            try:
                if modeNumber == "2":
                    maxNumber = int(random.randint(1,64))
                elif modeNumber == "3":
                    maxNumber = int(input("Введите целое число, для случайного числа до данного диапазона: "))
                else:
                    maxNumber = 10
                numN = int(random.randint(1, maxNumber))
            except:
                print("Введённое в строку, не было целым числом.")
                trueFalse2 = True
        return numN
    else: pass

while(True):
    inputString = str(input("Выберите режим:\n1 = Ручной ввод.\n2 = Рандомное число.\n3 = Рандомное число, ручной ввод для диапазона случайного числа.\n4, й, q = Выход из программы\nВвод: "))
    if inputString in ["1","2","3"]:
        result = runCode(inputString)
        listArrayNumber = [runFactorial(i) for i in range(1,result+1)]
        print(listArrayNumber)
    elif inputString.lower() in ["4","q","й"]:
        print("Выход из программы")
        break
    else:
        pass


