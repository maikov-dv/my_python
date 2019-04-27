# определение суммы квадратов нечетных цифр в числе

number = input("Введите число: ")
result = 0
for i in number:
    if int(i) % 2 == 0:
        continue
    result += pow(int(i), 2)
print("Результат:", result)
