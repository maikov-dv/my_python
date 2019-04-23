# угадывание случайного целого числа

import random

random_number = random.randint(1, 4)
user_number = int(input("Введите целое число от 1 до 4: "))

if user_number == random_number:
    print("Победа!")
else:
    if random_number > user_number:
        print("Загаданное число больше!")
    elif random_number < user_number:
        print("Загаданное число меньше!")
