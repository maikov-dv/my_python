# вычисление значения функции

import math

x = float(input("Введите число: "))

def func_sinus(x):
    if 0.2 <= x <= 0.9:
        return math.sin(x)
    else:
        return 1
