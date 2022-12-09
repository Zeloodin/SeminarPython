import math, time

def TheTestRun():
    from time import time

    print("""
for x in range(35000000): # ~ 6.995173454284668
    n = f"{x:0b}"
    # strN = f"x = {x:0b}"

print(time() - begTime)
begTime = time()""")

    begTime = time()


    for x in range(35000000): # ~ 6.995173454284668
        n = f"{x:0b}"
        # strN = f"x = {x:0b}"

    print(time() - begTime)
    print(end="\n"*3)

    print('''
for x in range(1000000): # ~ 0.18949294090270996
    n = f"{x:0b}"
    # strN = f"x = {x:0b}"''')

    begTime = time()

    for x in range(1000000): # ~ 0.18949294090270996
        n = f"{x:0b}"
        # strN = f"x = {x:0b}"

    print(time() - begTime)
    print(end="\n"*3)

    print('''
for x in range(1000000): # ~ 6.318100214004517
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    # strN = f"x = {n}"''')

    begTime = time()

    for x in range(1000000): # ~ 6.318100214004517
        n = ""
        while x > 0:
            y = str(x % 2)
            n = y + n
            x = int(x / 2)
        # strN = f"x = {n}"
    print(time() - begTime)
    print(end="\n"*3)

    print('''
def ConvToIntBin(num):
    return int(f"{num:0b}")

for x in range(1000000): # ~ 0.340090274810791
    n = ConvToIntBin(x)
    # strN = f"x = {n}"''')

    begTime = time()

    for x in range(1000000): # ~ 0.340090274810791
        n = ConvToIntBin(x)
        # strN = f"x = {n}"
    print(time() - begTime)

# TheTestRun()



def ConvToIntBin(num):
    return int(f"{num:0b}")

min = 1
max = 10000000000000000000000000000000000000000000000000000000000000000
step = 0
n = min
count = 0
levelUp = 0
overResult = 0
while(count < max):
    count += 1
#    overResult += 0.00000000001 * count + (overResult*0.00000001) # 0.00000000001
    overResult += 0.00000000001 * count + (overResult*0.00000001) # 0.00000000001
    plusN = 0
    try:
        summaN = n
        plusN = 0
        levelUp += float((0.01 * (count / n)) * (1 + overResult))
        if levelUp > 0:
            pass
        else:
            levelUp *= float(0.95)

        for i in range(len(str(summaN))):
#            if (count/n) < 0.000008 and (0 < levelUp >= 1):
#                plusN = float(plusN + ((summaN % 10) * levelUp*10000) * (1 + overResult))
#                levelUp = float(levelUp - (levelUp*100) * (1 + overResult))
#            else:
#                plusN = float(plusN + ((summaN%10)*levelUp) * (1 + overResult))
            plusN = float(plusN + ((summaN%10)*levelUp) * (1 + overResult))
            summaN //=10

        step = float(len(str(n)) + plusN)

    except (ZeroDivisionError, ValueError, TypeError): pass


    if (int(count) % 1 == 0): # 10000
        print(f"count:{count}, n:{int(n)}, plusN:{int(plusN)}, levelUp:{levelUp}, step:{int(step)}, {count / n}, overResult:{overResult}")
    # print(f"count:{count}, n:{n}, plusN:{plusN}, levelUp:{levelUp}, step:{step}, {count / n}, ConvToIntBin(n):{ConvToIntBin(n)}")
    n += step






# Создаёт список от 0 до 16777215. Очень медленно. Очень не выгодно. Не рекомендуемо.
# binaryList = [str((n0*1)+
#                   (n1*10)+
#                   (n2*100)+
#                   (n3*1000)+
#                   (n4*10000)+
#                   (n5*100000)+
#                   (n6*1000000)+
#                   (n7*10000000)+
#                   (n8*100000000)+
#                   (n9*1000000000)+
#                   (n10*10000000000)+
#                   (n11*100000000000)+
#                   (n12*1000000000000)+
#                   (n13*10000000000000)+
#                   (n14*100000000000000)+
#                   (n15*1000000000000000)+
#                   (n16*10000000000000000)+
#                   (n17*100000000000000000)+
#                   (n18*1000000000000000000)+
#                   (n19*10000000000000000000)+
#                   (n20*100000000000000000000)+
#                   (n21*1000000000000000000000)+
#                   (n22*10000000000000000000000)+
#                   (n23*100000000000000000000000))
# for n23 in range(0, 2)
# for n22 in range(0, 2)
# for n21 in range(0, 2)
# for n20 in range(0, 2)
# for n19 in range(0, 2)
# for n18 in range(0, 2)
# for n17 in range(0, 2)
# for n16 in range(0, 2)
# for n15 in range(0, 2)
# for n14 in range(0, 2)
# for n13 in range(0, 2)
# for n12 in range(0, 2)
# for n11 in range(0, 2)
# for n10 in range(0, 2)
# for n9 in range(0, 2)
# for n8 in range(0, 2)
# for n7 in range(0, 2)
# for n6 in range(0, 2)
# for n5 in range(0, 2)
# for n4 in range(0, 2)
# for n3 in range(0, 2)
# for n2 in range(0, 2)
# for n1 in range(0, 2)
# for n0 in range(0, 2)]
# print(binaryList[16777215],len(binaryList)-1)
