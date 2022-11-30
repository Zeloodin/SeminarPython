# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
#Пример:
#
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# def ConvToIntBin(num):
#     return int(f"{num:0b}")

inputNumber = int(input())
dec2binNumber = (bin(inputNumber)[2:].zfill(4).replace('b', '0'))
print(dec2binNumber)

exec("inputNumber = int(input())\ndec2binNumber = (bin(inputNumber)[2:].zfill(4).replace('b', '0'))\nprint(dec2binNumber)")

exec("print((bin(int(input()))[2:].zfill(4).replace('b', '0')))")


# print(bin(inputNumber)[2:].zfill(12))
# print(bin(inputNumber)[2:].zfill(24))
# print(bin(inputNumber)[2:].zfill(8))
#
# print(bin(inputNumber)[2:].zfill(8).replace('b', '0'))
#
# x = bin(inputNumber)
# print(x)
# print(x[2:])
#
# print(f"{inputNumber:0b}")
# print(ConvToIntBin(inputNumber))
#
# # print([ConvToIntBin(i) for i in range(255+1)])