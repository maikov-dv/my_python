# todo list

global_task = []
global_category = []
global_date = []

while True:
    print("Простой todo:\n", "1. Добавить задачу.\n", "2. Вывести список задач\n", "3. Выход.\n")
    action_number = int(input("Укажите число: "))
    task_list = []
    category_list = []
    date_list = []
    if action_number == 1:
        task = input("Сформулируйте задачу: ")
        category = input("Добавьте категорию к задаче: ")
        date = input("Добавьте время к задаче: ")
        global_task.append(task_list.append(task))
        global_category.append(category_list.append(category))
        global_date.append(date_list.append(date))
    elif action_number == 2:
        for i in global_task:
            print("Задача:", task, "Категория: ", category, "Дата:", date)
    elif action_number == 3:
        print("Вы вышли из программы!")
        break
    else:
        print("Ошибка ввода!")
