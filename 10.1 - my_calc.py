def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    chosen_operator = input("Введите оператор: ")
    if chosen_operator == "+":
        print(add(a, b))
    elif chosen_operator == "-":
        print(sub(a, b))
    elif chosen_operator == "*":
        print(mul(a, b))
    elif chosen_operator == "/":
        print(div(a, b))
    else:
        print("Неправильно введен оператор!!!")
except ZeroDivisionError:
    print("Ошибка деления на ноль!!!")
except ValueError:
    print("Ошибка преобразования типа!!!")
