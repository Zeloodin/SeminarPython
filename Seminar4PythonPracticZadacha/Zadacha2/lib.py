import os.path

def IsInteger(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def IsIntegerNumber(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

def IsNaturalNumber(num):
    isPrimeNum = True
    minN = num
    for i in range(1,num+1):
        if IsIntegerNumber(num/i) and minN > int(num/i) and num/i != 1:
            minN = int(num/i)
            isPrimeNum = False
    return isPrimeNum

def CreateListPrimeNumber(minlen,maxlen=2):
    if minlen > maxlen:
        tempnum = maxlen
        maxlen = minlen
        minlen = tempnum
    elif minlen < 2:
        maxlen = 1
        minlen = 1
    return [i for i in range(minlen,maxlen+1) if IsNaturalNumber(i)]

def CreateListPrimeNumberFileText(minlen,maxlen=2,txtNameFile= "listPrimeNumber", mode="w"):
    if minlen > maxlen:
        tempnum = maxlen
        maxlen = minlen
        minlen = tempnum
    elif minlen < 2:
        maxlen = 1
        minlen = 1
    textFile = open(f"{txtNameFile}.txt", mode)
    textFile.write("")
    textFile.close()
    for i in range(minlen,maxlen+1):
        if IsNaturalNumber(i):
            with open(f'{txtNameFile}.txt', 'a+') as fileText:
                fileText.write(str(i))
                fileText.write('\n')

# def CheckListPrimeNumber(listPrimeNumber):
#     isFileEmpty = True
#     listN = []
#     listPrimeNumberSplit = listPrimeNumber.split("\n")
#     lenghtListPrime = len(listPrimeNumberSplit)
#     for k in range(0,lenghtListPrime):
#         if listPrimeNumberSplit[k] != "" and IsInteger(listPrimeNumberSplit[k]):
#             listN.append(int(listPrimeNumberSplit[k]))
#             isFileEmpty = False
#     if isFileEmpty:
#         print("файл пуст")
#         return listN
#     else:
#         return listN

def ListCheck(listNum):
    listPrm = CreateListPrimeNumber(listNum[-1])
    falseIndex = []
    try:
        for i in range(len(listPrm)):
            if listPrm[i] != listNum[i]:
                falseIndex.append(i)
    except IndexError:
        return falseIndex
    return falseIndex

# def CheckIndexNumberPrime(listNum,falseIndex):
#     textFile = open(f"listPrimeNumber_copy.txt", "r")
#     listPrimeNumber = textFile.read().split("\n")
#     textFile.close()
#     for indx in falseIndex:
#         listNum[indx] = int(listPrimeNumber[indx])
#     return listNum

# def FullCheckAndFix(txtNameFile= "listPrimeNumber", listNum = None):
#     if listNum == None:
#         textFile = open(f"{txtNameFile}.txt", "r")
#         listPrimeNumber = textFile.read()
#         textFile.close()
#         listNum = CheckListPrimeNumber(listPrimeNumber)
#
#     arrrayList = ListCheck(listNum)
#     listNumCheckingFix = CheckIndexNumberPrime(listNum,arrrayList)
#     return listNumCheckingFix

# def UpdateListPrimeNumber(txtNameFile= "listPrimeNumber"):
#     textFile = open(f"{txtNameFile}.txt", "r")
#     listPrimeNumber = textFile.read()
#     textFile.close()
#
#     listNum = CheckListPrimeNumber(listPrimeNumber)
#     # CreateListPrimeNumberFileText(listNumMaxLen)
#     listNumCheckingFix = FullCheckAndFix(listNum = listNum)
#
#     textFile = open(f"{txtNameFile}.txt", "w")
#     textFile.write("\n".join(listNumCheckingFix))
#     textFile.close()



def AddListPrimeNumber(txtNameFile= "listPrimeNumber"):
    if not os.path.isfile(f"{txtNameFile}.txt"):
        textFile = open(f"{txtNameFile}.txt", "w")
        textFile.close()
        print(f"Текстовый файл под названием, {txtNameFile}.txt, был создан")
    else: print(f"Уже существует текстовый файл под названием, {txtNameFile}.txt")


# print(UpdateListPrimeNumber())