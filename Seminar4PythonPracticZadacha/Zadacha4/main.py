# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл (или вывести в терминал) многочлен степени k.
#
#Пример:
#
# k = 2  => 2*x^2 + 4*x + 5
#
# k = 3  => 41*x^3 + 6*x^2 + 2*x + 98

from os import path
from random import randint




def CheckList(txtNameFile= "GenZadacha",showPrint = False):
    if not path.isfile(f"{txtNameFile}.txt"):
        textFile = open(f"{txtNameFile}.txt", "a+")
        textFile.close()
        if showPrint:
            print(f"Текстовый файл под названием, {txtNameFile}.txt, был создан")



def GenZadacha(k, randMin, randMax, save, txtNameFile= "GenZadacha"):
    textZadacha = ""
    textZadacha += str(randint(randMin,randMax))
    for i in range(1,k):
        if i == 1:
            textZadacha = f"{randint(randMin,randMax)}*x + {textZadacha}"
        elif i > 1:
            textZadacha = f"{randint(randMin,randMax)}*x^{i} + {textZadacha}"
    # print(textZadacha)
    if save:
        textFile = open(f"{txtNameFile}.txt", "a+")
        textFile.write(textZadacha+"\n")
        textFile.close()

        textFile = open(f"{txtNameFile+'_K'}.txt", "a+")
        textFile.write(f"k = {k}  => {textZadacha}" + "\n")
        textFile.close()
    return textZadacha


def GenerateZadacha(k,count,save=False,txtNameFile= "GenZadacha",randMin=0,randMax=100):
    if type(k) == list:
        pass
    elif type(k) == int:
        k = [k]
    else: k = [k]
    if count < len(k): count = len(k)
    count = int(int(count)/len(k))
    CheckList(txtNameFile=txtNameFile,showPrint=False)
    CheckList(txtNameFile=txtNameFile+"_K", showPrint=False)
    allText = ""
    for ik in k:
        if ik < 1: pass
        else:
            for j in range(count):
                textZadacha = GenZadacha(k=ik+1, randMin=randMin, randMax=randMax,save=save,txtNameFile=txtNameFile)
                print(f"k = {ik}  => {textZadacha}")
                allText = f"k = {ik}  => {textZadacha}" + "\n" + allText
    return allText

def GenArrNum(k,kmx = 0):
    if kmx == True and type(kmx) != int: kmx = k
    elif kmx == False and type(kmx) != int: kmx = 0
    elif type(kmx) == int: pass
    else: kmx = 0
    if k < 1: k = 1
    if k > kmx:
        tempN = kmx
        kmx = k
        k = tempN
    return [i for i in range(k,kmx+1)]

arraN = 2#GenArrNum(2,3)
count = 100
maxRandGen = 99
minRandGen = 1
GenerateZadacha(arraN,count,save=True,randMin=minRandGen,randMax=maxRandGen)

