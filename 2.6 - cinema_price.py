# определение стоимости билетов в кино с учетом скидок

film = str(input("Выбрать фильм: "))
date = str(input("Выбрать дату (сегодня, завтра): "))
time = int(input("Выбрать время: "))
tickets = int(input("Указать количество билетов: "))
print("Ваш выбор:", "фильм - ", film, ", дата - ", date, ", время - ", time, ", количество билетов - ", tickets)
if film == "Пятница":
    if date == "сегодня":
        if time == 12:
            if tickets >= 20:
                print("Стоимость: ", tickets * 250 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 250, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 16:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 20:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450, " руб")
            else:
                print("Неправильно указано количество билетов!")
        else:
            print("Неправильно указано время!")
    elif date == "завтра":
        if time == 12:
            if tickets >= 20:
                print("Стоимость: ", tickets * 250 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 250 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 16:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 20:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450 * 0.95, " руб")
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
                print("Стоимость: ", tickets * 250 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 250, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 13:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 16:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350, " руб")
            else:
                print("Неправильно указано количество билетов!")
        else:
            print("Неправильно указано время!")
    elif date == "завтра":
        if time == 10:
            if tickets >= 20:
                print("Стоимость: ", tickets * 250 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 250 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 13:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 16:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350 * 0.95, " руб")
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
                print("Стоимость: ", tickets * 350 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 14:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 18:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450, " руб")
            else:
                print("Неправильно указано количество билетов!")
        else:
            print("Неправильно указано время!")
    elif date == "завтра":
        if time == 10:
            if tickets >= 20:
                print("Стоимость: ", tickets * 350 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 350 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 14:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        elif time == 18:
            if tickets >= 20:
                print("Стоимость: ", tickets * 450 * 0.95 * 0.8, " руб")
            elif 0 <= tickets < 20:
                print("Стоимость: ", tickets * 450 * 0.95, " руб")
            else:
                print("Неправильно указано количество билетов!")
        else:
            print("Неправильно указано время!")
    else:
        print("Неправильно указана дата!")
else:
    print("Неправильно указан фильм!")
