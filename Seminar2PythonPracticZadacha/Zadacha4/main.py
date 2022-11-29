# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

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

def RunSum(count = 0):
    if count != 0: sum = [i if i%2==0 else 0  for i in range(1,count+1)]
    else: sum = [i if i%2==0 else 0  for i in range(1,inputIntNum()+1)]
    result = 0

    try:
        for i in range(len(sum)):
            if sum[i] == 0:
                del sum[i]
    except: pass

    for num in sum:
        result += num

    stringSum = sum
    for n in range(len(stringSum)):
        stringSum[n] = str(stringSum[n])

    print(f"|   {result}   |  {count} | {sum} | {'+'.join(stringSum)}={result} |")  # ,count)#,sum)

    # Это надо улучшить. Интересная идея.
    # from time import sleep
    # for i in range(10000):
    #     progress = (4-len(str(i)))*"0"+str(i)
    #     sleep(0.01)
    #     print(end="\n"*100)
    #     print("|-----------------------------------------------------------------------|_| |X|")
    #     print("|NameCode| len |--------------------------------------------------------------|")
    #     print("| RESULT |count|------------result----------------------|---------------------|")
    #     print("|--------|-----|----------------------------------------|---------------------|")
    #     print(f"|   {result}   |  {count} | {sum} | {'+'.join(stringSum)}={result} |")
    #     print("|--------|-----|----------------------------------------|---------------------|")
    #     print(f"|Progress|{progress}%|----------------------------------------|---------------------|")
    #     print("|-----------------------------------------------------------------------------|")
    #     print(end="\n"*2)




RunSum()