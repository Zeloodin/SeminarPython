#!/usr/bin/env python
# -*- coding: utf-8 -*-

def IsNumReal(n):
    isNumberReal = list("0123456789.")
    for i in list(str(n)):
        if not i in isNumberReal:
            return False
    return True

def IsNumInt(n):
    isNumberInt = list("0123456789")
    for i in list(str(n)):
        if not i in isNumberInt:
            return False
    return True

def IsDouble(strText,findSymbol):
    doubleSymbol = False
    for i in range(len(strText)):

        # try:
        #     if strText[i - 1] in signs and strText[i] == "-" and strText[i - 1] == "-" and IsNumReal(strText[i - 2]):
        #         doubleSymbol = True
        # except IndexError: pass

        # try:
        #     if strText[i - 2] in signs and strText[i - 1] == "-" and IsNumReal(strText[i]):
        #         doubleSymbol = False
        #         return doubleSymbol
        # except IndexError: pass
        #
        # try:
        #     if strText[i - 1] in signs and strText[i] == "-" and IsNumReal(strText[i + 1]):
        #         doubleSymbol = False
        #         return doubleSymbol
        # except IndexError: pass
        #
        # try:
        #     if IsNumReal(strText[i - 1]) and strText[i] in signs and strText[i + 1] == "-" and IsNumReal(strText[i + 2]):
        #         doubleSymbol = False
        #         return doubleSymbol
        # except IndexError: pass
        #
        try:
            if IsNumReal(strText[i - 2]) and strText[i - 1] in signs and strText[i] == "-" and IsNumReal(strText[i + 1]):
                doubleSymbol = False
                return doubleSymbol
        except IndexError: pass

        try:
            if strText[i] == findSymbol and strText[i + 1] == findSymbol:
                doubleSymbol = True
                return doubleSymbol
        except IndexError: pass

    return doubleSymbol

def FilterClearSymbol(strText):
    strText = strText.replace(" ", "")
    strText = strText.replace("**", "^")
    doubleSymbol = list("+-*/\.=^")
    for symLenght in range(len(doubleSymbol)-1):
        findSymbol = doubleSymbol[symLenght]
        doubleSym = True # Enable/Disable Clear Double Sign
        while(doubleSym):
            i = 0
            while(i<len(strText)):
                if findSymbol == strText[i]:
                    j = i+1
                    while(j<len(strText)):
                        # print(strText," "*35,f"||{strText[:j]}[{j}=={strText[j]}]{strText[j+1:]}||",j,findSymbol,strText[j])
                        #
                        #
                        # if strText[j] in signs and strText[j + 1] == "-" and strText[j + 2] == "-":
                        #     print(f"|||{strText[:j + 0] + strText[j + 1:]} ||2\n|||{strText} ||1")
                        #     # strText = strText[:j]+strText[j+1:]
                        #     break
                        #
                        # elif strText[j] == "-" and IsNumReal(strText[j+1]):
                        #     break
                        #
                        # elif findSymbol == strText[j]:
                        if findSymbol == strText[j]:
                            strText = strText[:j]+strText[j+1:]
                        else:
                            break
                i += 1
            doubleSym = IsDouble(strText,findSymbol)
    return strText

def CleanString(strText):
    strText = str(FilterClearSymbol(strText))
    splitText = list(str(strText).replace("\\",'/'))
    return splitText

def JoinSplit(strText):
    arrText = CleanString(strText)
    # print(arrText)
    for n in range(len(arrText) - 1, 0, -1):
        if IsNumReal(arrText[n]):
            if IsNumReal(arrText[n - 1]):
                arrText[n - 1] += str(arrText[n])
                arrText.pop(n)
    return arrText

def NumberOperation(arrValue,operat):
    try:
        match operat:
            case "^":
                return float(arrValue[0])**float(arrValue[1])
            case "*":
                return float(arrValue[0])*float(arrValue[1])
            case "/":
                return float(arrValue[0])/float(arrValue[1])
            case "+":
                return float(arrValue[0])+float(arrValue[1])
            case "-":
                return float(arrValue[0])-float(arrValue[1])
            case _:
                return ""
    except OverflowError:
        print("Результат слишком большой")
        return ''
    except ValueError:
        print("Не удалось преобразовать строку в число с плавающей запятой")
        return ''
    except ZeroDivisionError:
        print("Деление числа на ноль")
        return ''


# Round brackets or parentheses: ( )
# Square brackets or brackets: [ ]
# Curly brackets or braces: { }

def CalcRun(inputStr = None,splitString = None):
    global signs
    signs = ["^", "*", "/", "+", "-"]
    brackets = [["(",")"],["[","]"],["{","}"]]
    if splitString == None:
        splitString = JoinSplit(inputStr)

    for bracket in brackets:
        while (bracket[0] in splitString) and (bracket[1] in splitString):
            i = 0
            minBr = ""
            maxBr = ""
            level = 0
            levelMax = 0
            while (i < len(splitString)):

                if splitString[i] == bracket[0] and minBr == "":
                    level += 1
                if level > levelMax: levelMax = level
                if splitString[i] == bracket[1] and maxBr == "":
                    level -= 1
                i += 1

            else:
                n = 0
                level = 0
                while(n < len(splitString)):
                    if splitString[n] == bracket[0] and minBr == "":
                        level += 1
                        if level == levelMax:
                            minBr = n
                    elif splitString[n] == bracket[1] and maxBr == "":
                        if level == levelMax:
                            maxBr = n
                        level -= 1
                    n += 1
                else:
                    try:
                        bracketSplit = splitString[minBr+1:maxBr]
                        bracketStringResult = ''
                        for sign in signs:
                            while (sign in bracketSplit):
                                ni = 0
                                while (ni < len(bracketSplit)):
                                    if sign == bracketSplit[ni]:
                                        bracketStringResult = NumberOperation([bracketSplit[ni - 1], bracketSplit[ni + 1]], bracketSplit[ni])
                                        bracketSplit.pop(ni)
                                        bracketSplit.pop(ni)
                                        bracketSplit[ni - 1] = bracketStringResult
                                    ni += 1
                        del splitString[minBr + 1:maxBr+1]
                        splitString[minBr] = bracketStringResult
                    except TypeError:
                        print("Скобки должны быть парными")
                        break

    for sign in signs:
        while (sign in splitString):
            i = 0
            while (i < len(splitString)):
                if sign == splitString[i]:
                    try:
                        result = NumberOperation([splitString[i - 1], splitString[i + 1]], splitString[i])
                        splitString.pop(i)
                        splitString.pop(i)
                        splitString[i - 1] = result
                    except IndexError:
                        print("Индекс списка вне допустимого диапазона")
                        try:
                            result = ""
                            splitString[i - 1] = result
                        except IndexError: pass
                i += 1
    return splitString

# # r"(5-(4+(2^14)))+5+((25+(2^5))/2)"
# while(True):
#     print('Console Calculator\nInput:',end="")
#     # inputStr = "(1-----1*(0-2*(5**3))----25)+255"#
#     inputStr = str(input())
#     result = "".join(CalcRun(inputStr))
#     print(result)












