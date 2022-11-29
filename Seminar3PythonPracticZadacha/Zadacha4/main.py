# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#Пример:
#
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ConvToIntBin(num):
    return int(f"{num:0b}")

print([ConvToIntBin(i) for i in range(255+1)])


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