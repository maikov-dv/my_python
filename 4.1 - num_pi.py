# вывод числа pi с определенным кол-вом знаков после запятой

import math

x = int(input("Введите целое число: "))

def pi_round(x):
    return f'Число Пи: {round(math.pi, x)}'

print(pi_round(x))
