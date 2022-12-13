
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# Если введённая строка является дробным или целым числом, цифры из числа суммируются, но перед суммированием, оно очищается от .,- символов.
# Иначе выдаёт 0, как и в строке присутствующие буквы, выдаст 0
inputFloat = lambda x=list(str(input("Введите дробное/целое число: "))): sum(map(int,filter(lambda x:(str(x) in str("123456789")),x if str("".join(x))
                                                   .replace(".","").replace(",","").replace("-","").isdigit() and len(str("".join(x))
                                                   .replace(",",".").split(".")) in [0,1,2] else "")))
print(inputFloat())

# Убирает всё, кроме чисел, и суммирует каждую цифру из введённого числа
# inputFloat = lambda x=list(str(input())) :  sum(map(int,filter(lambda x:(str(x) in str("123456789")),x)))
# print(inputFloat())

# import re
# input = input()
# # re.sub(r'[^0-9.]+', r'', string)
# inputFloat = lambda x=re.sub(r"[^0-9]+",r"", input):sum(map(int,x))
# print(inputFloat())
#
# inputFloat = lambda x=list(str(input)):  sum(map(int,filter(lambda x:(str(x) in str("123456789")),x))) # ("0123456789")
# print(inputFloat())
#
# inputFloat = lambda x=list(str(input)):  sum(map(int,filter(lambda x:(str(x) in ["1","2","3","4","5","6","7","8","9"]),x))) # ["0","1","2","3","4","5","6","7","8","9"]
# print(inputFloat())