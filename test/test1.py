import glob
from random import randint,sample



# f1 = lambda x: [randint(0,1) for i in range(x)]
# f2 = lambda x: sum(x) == len(x)
# f3 = lambda x,mx=5: [f2(f1(x)) for i in range(mx)]
# maxRepeat = 10000
# count = 2
# result = f3(count,maxRepeat)
# print(f"Из {count} человек, с {sum(result)/len(result)} шансом, что все поднимут руки. Повторов {sum(result)} из {maxRepeat}, поднимут руки")

from decimal import Decimal
from time import time

# tm = time()

# for i in range(1,101):
#     print(time() - tm, end="	")
#     tm = time()
#     result = 0
#     maxRepeat = 1
#     count = 10**i
#     while(int(result) < 1):
#
#         result = maxRepeat/2**count
#         maxRepeat *= Decimal(10)
#     print(count, result, maxRepeat,sep="	")

# 0.000000000002001407899955310000
# 0.|000|000|000|002|001|407|899|955|310|000|

# 0.0	10	9.765625	100000
# 0.0	100	7.888609052210118054117285653	1.000000000000000000000000000E+32
# 0.0	1000	9.332636185032188789900895447	1.000000000000000000000000000E+303
# 0.0019948482513427734	10000	5.012372749206452009297555934	1.000000000000000000000000000E+3012
# 1.992666482925415	100000	1.000998903798694166816264713	1.000000000000000000000000000E+30104
# 1958.54394698143

# decN = 1
decList = []#[decN]
[decList.append(0) for i in range(10)]
print(decList)
end = True
while(end):
    decList[0]+=1
    for i in range(len(decList)):
        if decList[-1] >= 1:
            end = False
            break
        elif decList[i] >= 10000 and i!=len(decList)-1 and i !=1 and i !=2 and i !=3 and i !=4 and i !=5:
            decList[i+1] += 1
            decList[i] = 0
        elif decList[i] >= 60 and i==1:
            decList[i + 1] += 1
            decList[i] = 0
        elif decList[i] >= 60 and i==2:
            decList[i + 1] += 1
            decList[i] = 0
        elif decList[i] >= 24 and i==3:
            decList[i + 1] += 1
            decList[i] = 0
        elif decList[i] >= 365 and i==4:
            decList[i + 1] += 1
            decList[i] = 0
        elif decList[i] >= 100 and i==5:
            decList[i + 1] += 1
            decList[i] = 0
    print([decList[i] for i in range(len(decList))])












