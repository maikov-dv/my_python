cinema_dict = {
    "Пятница": {12: 250, 16: 350, 20: 450},
    "Чемпионы": {10: 250, 13: 350, 16: 350},
    "Пернатая банда": {10: 350, 14: 450, 18: 450}
    }

film = input("Выбрать фильм: ")
date = input("Выбрать дату (сегодня, завтра): ")
time = int(input("Выбрать время: "))
tickets = int(input("Указать количество билетов: "))
print("Ваш выбор:", "фильм - ", film, ", дата - ", date, ", время - ", time, ", количество билетов - ", tickets)

if cinema_dict.get(film, 'нет фильма') != 'нет фильма':
    if film == "Пятница":
        if date == "сегодня":
            if time == 12:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][12] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][12] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 16:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][16] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][16] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 20:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][20] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][20] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        elif date == "завтра":
            if time == 12:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][12] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][12] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 16:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][16] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][16] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 20:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пятница"][20] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пятница"][20] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        else:
            print("Неправильно указана дата!")
    elif film == "Чемпионы":
        if date == "сегодня":
            if time == 10:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][10] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][10] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 13:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][13] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][13] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 16:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][16] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][16] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        elif date == "завтра":
            if time == 10:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][10] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][10] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 13:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][13] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][13] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 16:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][16] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Чемпионы"][16] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        else:
            print("Неправильно указана дата!")
    elif film == "Пернатая банда":
        if date == "сегодня":
            if time == 10:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][10] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][10] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 14:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][14] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][14] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 18:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][18] * tickets * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][18] * tickets, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        elif date == "завтра":
            if time == 10:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][10] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][10] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 14:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][14] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][14] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            elif time == 18:
                if tickets >= 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][18] * tickets * 0.95 * 0.8, " руб")
                elif 0 <= tickets < 20:
                    print("Стоимость: ", cinema_dict["Пернатая банда"][18] * tickets * 0.95, " руб")
                else:
                    print("Неправильно указано количество билетов!")
            else:
                print("Неправильно указано время!")
        else:
            print("Неправильно указана дата!")
else:
    print('Неправильно указан фильм!')
