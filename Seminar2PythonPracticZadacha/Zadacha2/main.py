# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
#
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

def inputIntNum(str = ""):
    if str != "": print(str)
    trueFalse = True
    numN = 0
    while(trueFalse):
        trueFalse = False
        try:
            numN = int(input("Введите целое число: "))
        except:
            print("Введённое в строку, не было целым числом.")
            trueFalse = True
    return numN

def findLowerNum(num):
    numInt = num
    for i in range(numInt,1,-1):
        if (num > num/i) and (num/i).is_integer() and not (num/i == 1):
            num = int(num/i)
    return num



def runNaturalCode(arrayListNumbers,naturalNumbers):
    listNaturalNumbers = []
    for i in arrayListNumbers:
        result = findLowerNum(i)
        # print(i," ",result)
        if naturalNumbers == True:
            if i == result:
                listNaturalNumbers.append(result)
                print(result)
        else:
            listNaturalNumbers.append(result)
    return listNaturalNumbers

def runCode(arrayListNumbers = None, naturalNumbers = False):
    if arrayListNumbers != None:
        listNaturalNumbers = runNaturalCode(arrayListNumbers,naturalNumbers)
        return listNaturalNumbers
    else:
        numberN = 0
        while(numberN <= 0):
            numberN = inputIntNum()
            if numberN <= 0: print("Это недопустимый номер. Попробуй ещё раз.")



        result = findLowerNum(numberN)
        print(result)


runCode()
# 300761, 970297, 410741, 161053, 1842853, 1585147, 1842877, 1842887, 1842889, 1842899, 13642801, 13642807
# 10000019, 10000079, 10000103, 10000121, 10000139, 10000141, 10000169, 10000189, 10000223
# 10000229, 10000247, 10000253, 10000261, 10000271, 9999937, 9999931, 14647723

#  14647702
# |	      \
# 7323851  2



# def ArrayNaturalNumberList(minN = None, maxN = None, naturalNumbers = False):
#     try:
#         if (type(minN) == str) or (minN is None):
#             minN = int(minN)
#     except: minN = 0
#     try:
#         if (type(maxN) == str) or (maxN is None):
#             maxN = int(maxN)
#     except: maxN = None
#     try:
#         if (type(naturalNumbers) == str) or (naturalNumbers is None):
#             naturalNumbers = bool(naturalNumbers)
#     except: naturalNumbers = False
#     # print(f"type({minN}){type(minN)}, type({maxN}){type(maxN)}, type({naturalNumbers}){type(naturalNumbers)}")
#
#
#     if type(naturalNumbers) is str:
#         naturalNumbers = int(naturalNumbers)
#     if naturalNumbers > 0 and type(naturalNumbers) is int:
#         naturalNumbers = True
#     elif naturalNumbers <= 0 and type(naturalNumbers) is int:
#         naturalNumbers = False
#
#
#     if minN in [None,0] and maxN is [None,0] and naturalNumbers is [False,0]:
#         minN = int(0)
#     elif str(naturalNumbers) == "True" and str(maxN) is ["True","False"] and str(minN) is ["True","False"]:
#         naturalNumbers = True
#         maxN = int(1)
#         minN = int(0)
#     elif str(naturalNumbers) == "False" and maxN == None and str(minN) in ["True","False"]:
#         maxN = int(minN)
#         minN = int(0)
#
#     if str(maxN) == "True" and minN != None:
#         naturalNumbers = True
#         maxN = None
#     elif str(maxN) == "False" and minN != None:
#         naturalNumbers = False
#         maxN = None
#
#     if str(minN) == "True" and maxN != None:
#         naturalNumbers = True
#         minN = int(0)
#     elif str(minN) == "False" and maxN != None:
#         naturalNumbers = False
#         minN = int(0)
#
#     if maxN == None and minN != None and not( str(maxN) is ["True","False"] and str(minN) is ["True","False"]):
#         maxN = int(minN)
#         minN = int(0)
#
#     if int(maxN) < int(minN) and not (minN == True or minN == False)\
#                    and not (maxN == True or maxN == False):
#         tempN = int(maxN)
#         maxN = int(minN)
#         minN = int(tempN)
#     else: pass
#
#
#
#     print(minN, maxN, naturalNumbers)
#     arraList = [i+1 for i in range(minN,maxN)]
#     # print(arraList)
#     print(runCode(arraList, naturalNumbers = naturalNumbers))
#
# # ArrayNaturalNumberList(21,5,True)
#
#
# patternTest = [0,"0",False,"False",1,"1",True,"True",None,"None",250,"250",-250,"-250"]
# for i in patternTest:
#     for j in patternTest:
#         for f in patternTest:
#             # print(f"{i},{j},{f}")
#             print(f"type({i}){type(i)}, type({j}){type(j)}, type({f}){type(f)}")
#             ArrayNaturalNumberList(i,j,f)