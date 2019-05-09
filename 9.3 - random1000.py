from random import randint

random_list = [randint(-1000000, 1000000) for i in range(1000)]

def count_negative_numbers(random_list):
    negative_numbers = []
    for item in random_list:
        if item < 0:
            negative_numbers.append(item)
    return len(negative_numbers)

print('Количество отрицательных элементов: ', count_negative_numbers(random_list))

