# вычисление значения функции

value = input("Введите значение параметра: ")
if value:
    x = float(value)
    if -2.4 < x < 5.7:
        print(pow(x, 2))
    else:
        print(4)
else:
    print("Вы не ввели значение параметра!")
