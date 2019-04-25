# функция по возврату строки в определенном виде

s = input("Введите строку: ")

n = int(input("Введите целочисленное значение: "))

def return_str_func(s, n):
    if len(s) > n:
        return s.upper()
    else:
        return s

print(return_str_func(s, n))
