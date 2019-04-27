result = 0
while True:
    num_or_stop = input("Введите число или слово 'стоп' для выхода: ")
    if num_or_stop == "стоп":
        print("Выход!")
        break
    elif num_or_stop.isdigit():
        result += int(num_or_stop)
    else:
        print("Ошибка ввода.")
print("Сумма:", result)
