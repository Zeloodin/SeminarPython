# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import time, datetime

# print([ord(n) for n in seed])

def RandomGenNumber():
    intSeedSplit = CreateListRandom()
    seed = intSeedSplit[0]
    intSeedSplit = CreateListRandom(seed)
    intSeed = intSeedSplit[1]
    isLen = True
    while (isLen):
        tempNum = intSeed % 10
        lenghtNum = int(str(tempNum) + ("0" * tempNum))
        intSeed = (intSeed // 10) + lenghtNum
        if len(str(intSeed)) > 8:
            isLen = True
        else:
            isLen = False

    return intSeed


def CreateListRandom(inSeed = "", inString = ""):
    isSeedInput = False
    if inSeed != "": isSeedInput = True

    now = datetime.datetime.now()
    dateString = str('%d-%d-%d-%d_%d-%02d-%02d-%d' % (
    now.year, now.month, now.isoweekday(), now.day, now.hour, now.minute, now.second, now.microsecond))

    if isSeedInput != True:
        seed = dateString +"""
        YXgee02gPOpA#cBiDtFlIeMYaSsmRCTmpN3ILl4S6p#uOR2fw3thSPTAO{rJym*Pyr|8LZkp4T}{O#vb*LqEfU?3@4BoSjGu3jIw5k0Hkkzif8ad7738Q49B
        sjl0z5Plt@gTE~j7rkAxLurzIz4rgTecudKDWxLB1Xwp5g~9hHttTV~gJ?7Xt%wGFd1*V$2i*0399WPt{pj08I24nCR5H~?KJyS~OJdy4wDW|KejE@GMAW8L
        J45xMMr6z$J6qK$V3MmagUN?FzIZE$p~%*DC?$M}b#%61$C3%jWrYNER05*0EKY7DXM|Qgzziag1wDcgL#Y52jPqGsmFg77hC}J2~F?f45SvC~UwrgrU$Hh%
        u$r3q@?F~MU5cl~q*0a~E~qF|0SZPa{W*lLnIpN@p#xaeezkTVfVd$~d0fTd0ZiDHwlpETc5K5Ew0GrjKTgF#2T0d#EwpcJynVVeDfWiXz9f|sQ7qqruz7%E
        SMFxc*hCI7Y~mxK1q{xEMt3@xtt#2JZZID88Mvl$svCJOO$Ibih@?frShE}~1|idSpkAZhPH*0I4YBaHgZ8K4gNA}rTe2NCyXbC{?#wUp0~KFEz?n{Av6JV$
        zxjAV0}g|kv?@4Mr3%UX@D$5E8@5MdDxtjTt4I4BsZJ72rV#nYJPVTEtYQF@u*H3sUpH*4ePvU9Xhbmf5p35$UTOzAarxz9r*c0reM|SMrrxSZwnaa5|UHvq
        UjoJo1}az80I|kpYW~nvaxL464DF4w6vdL9cBWl#8Z%{OxoORkW4DfndD7HQbb{g}GBo#wIXFh*mnK5MO%e7reTcoj1{9vf1xSh~}ICc2wBtznX9susA#~nk
        WvwMQtgYnhX84duf|YDW*?%KWl~@$Mjux~|DmvxX*B|F7mj$~m@0yezfODWNp6#q%KeHheFR3~yId1RfK~Oe6KcaLXcIQN~eiJx54HQTSjLFwfT|q7L#2?NL
        #ac6nI0cQDICfS4#4ULQKzZ4BQ$dt9
        """
    else:
        seed = (inString+inSeed+dateString)[0:2000] # [0:1050]

    intSeed = [str(ord(n)) for n in seed]
    intSeed = int("".join(intSeed))
    return seed, intSeed

def GetMax(array):
    for i in range(len(array)):
        array[i] = round(float(str(array[i]).split(("."))[1])*0.01,2)
    return max(array)

def GetMin(array):
    for i in range(len(array)):
        array[i] = round(float(str(array[i]).split(("."))[1])*0.01,2)
    return min(array)

listNums = [float(round((RandomGenNumber() % 100000) * 0.001, 2)) for i in range(5)]
print(f"{listNums} => {round(GetMax(listNums)-GetMin(listNums),2)} | Max: {GetMax(listNums)} | Min: {GetMin(listNums)}")










