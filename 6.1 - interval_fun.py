total = 0
for x in range(10, 31, 2):
    def func(x):
        return pow(x, 2) + 3
    total += func(x)
print("Сумма:", total)
