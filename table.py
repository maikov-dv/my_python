# название химического элемента по его атомному номеру

value = input("Введите атомный номер элемента из периодической таблицы химических элементов:\n")
if value:
    atomic_number = int(value)
    if atomic_number == 3:
        print("Li")
    elif atomic_number == 25:
        print("Mn")
    elif atomic_number == 80:
        print("Hg")
    elif atomic_number == 17:
        print("Cl")
    else:
        print("Неизвестный атомный номер!!!")
else:
    print("Введите атомный номер!")
