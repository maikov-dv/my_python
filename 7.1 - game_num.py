# угадай случайное число с 3 попыток

import random

computer_number = random.randint(1, 10)
print("Компьютер загадал число!\n", "У Вас есть 3 попытки. Удачи!")

number_of_chances = [1, 2, 3]
for chance in number_of_chances:
    if chance < 3:
        user_number = input("Попробуйте угадать число: ")
        if user_number == "выход":
            print("Игра завершена!")
            break
        elif computer_number == int(user_number):
            print("Победа!")
            break
        elif computer_number > int(user_number):
            print("Попробуйте число больше!")
        elif computer_number < int(user_number):
            print("Попробуйте число меньше!")
    elif chance == 3:
        user_number = input("Попробуйте угадать число: ")
        if user_number == "выход":
            print("Игра завершена!")
            break
        elif computer_number == int(user_number):
            print("Победа!")
            break
        elif computer_number != int(user_number):
            print("Game over!\n", "Загаданное число:", computer_number)
            break
