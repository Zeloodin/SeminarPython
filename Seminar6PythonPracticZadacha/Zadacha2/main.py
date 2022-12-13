
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]


arr_l = [12,'sadf',5643]
arr=[list() for i in range(2)]
fuct_lambda = lambda x: list(filter(lambda x:  arr[0].append(x) if type(x) == str else arr[1].append(x) if type(x) in [float,int] else None, x))
fuct_lambda(arr_l)
print(arr_l,"-->",", ".join(map(str, arr)))