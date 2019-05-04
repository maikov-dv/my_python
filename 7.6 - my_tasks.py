# todo list

global_task = []

while True:
    print('''Простой todo:
    1. Добавить задачу.
    2. Вывести список задач
    3. Выход.
    ''')
    action_number = input("Укажите число: ")
    if action_number == '1':
        task_list = []
        task = input("Сформулируйте задачу: ")
        task_list.append(task)
        category = input("Добавьте категорию к задаче: ")
        task_list.append(category)
        date = input("Добавьте время к задаче: ")
        task_list.append(date)
        global_task.append(task_list)
    elif action_number == '2':
        if global_task == []:
            print("Задач еще нет!")
        else:
            for i in global_task:
                print("Задача:", i[0], "Категория: ", i[1], "Дата:", i[2])
    elif action_number == '3':
        print("Вы вышли из программы!")
        break
    else:
        print("Ошибка ввода!")
