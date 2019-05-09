# todo list with dict

global_task = []

while True:
    print('''Простой todo:
    1. Добавить задачу.
    2. Вывести список задач
    3. Выход.
    ''')
    action_number = input("Укажите число: ")
    if action_number == '1':
        task_list = {}
        task = input("Сформулируйте задачу: ")
        task_list['name'] = task
        category = input("Добавьте категорию к задаче: ")
        task_list['categ'] = category
        date = input("Добавьте время к задаче: ")
        task_list['time'] = date
        global_task.append(task_list)
    elif action_number == '2':
        if global_task == []:
            print("Задач еще нет!")
        else:
            for i in global_task:
                print("Задача:", i['name'])
                print("Категория: ", i['categ'])
                print("Дата:", i['time'])
    elif action_number == '3':
        print("Вы вышли из программы!")
        break
    else:
        print("Ошибка ввода!")
