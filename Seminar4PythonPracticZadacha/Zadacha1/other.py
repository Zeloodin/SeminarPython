# https://github.com/Tuzliz/HW4_Phyton/blob/37a37f0d8769d4993c223e50f4bc25055fd0df3f/task1.py

#- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi, а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.

#Пример:
#- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1

#Ряд Нилаканта:
# π = 3 + 4/(2*3*4) — 4/(4*5*6) + 4/(6*7*8) — 4/(8*9*10) + 4/(10*11*12) — (4/(12*13*14) …
pi = 3.141
num1 = 2
num2 = 3
num3 = 4
for i in range(3):
    pi += 4 / (num1 * num2 * num3)
    num1 += 2
    num2 += 2
    num3 += 2
    pi -= 4 / (num1 * num2 * num3)
    num1 += 2
    num2 += 2
    num3 += 2

print(f'Число Пи при помощи формулы Нилаканта: {round(pi-0.141, 3)}')



# https://github.com/fmkorolev/HW_4/blob/522eb90d11ac920287c2d3446c2be2e803bc934b/hw%204.py

#  Задание 1- Вычислить число c заданной точностью d.
# Число Пи не просто обрезать с math.pi, а вычислить, используя формулы:
# Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
# Пример:
# - при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-

d = int(input('Введите точность: '))
calc_pi = 0
check = 0

for n in range(int(10000)):
    calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
    if abs(check - calc_pi) < 10**(-d):
        break
    check = calc_pi

print('pi = ', round(calc_pi, d))























