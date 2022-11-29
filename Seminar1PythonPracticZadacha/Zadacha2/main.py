# 2. (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# NOT (X OR Y OR Z) == (NOT X AND  NOT Y AND  NOT Z)

x1 = int
y1 = int
z1 = int
intBool = [0,1] #[i for i in range(2)]
for x1 in intBool:
    for y1 in intBool:
        for z1 in intBool:
            print(f"x = {x1}, y = {y1}, z = {z1}", end="  -=>->  ")
            print(f"if not ({x1} or {y1} or {z1}) == (not {x1} and not {y1} and not {z1})", end="  -=>->  ")
            print(f"if {not (x1 or y1 or z1)} == ({not x1} and {not y1} and {not z1})", end="  -=>->  ")
            # print(f"if {not (x1 or y1 or z1)} == ({not x1 and not y1 and not z1})", end="  -=>->  ")
            print(not (x1 or y1 or z1) == (not x1 and not y1 and not z1))