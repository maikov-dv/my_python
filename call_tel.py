# стоимость переговоров в разных городах

city_code = int(input("Введите код города: "))
call_duration = float(input("Введите длительность переговоров, в минутах: "))
if city_code == 343:
    print("В Екатеринбурге Ваша стоимость составит:", call_duration * 15, "руб")
elif city_code == 381:
    print("В Омске Ваша стоимость составит:", call_duration * 18, "руб")
elif city_code == 473:
    print("В Воронеже Ваша стоимость составит:", call_duration * 13, "руб")
elif city_code == 485:
    print("В Ярославле Ваша стоимость составит:", call_duration * 11, "руб")
else:
    print("Наша компания не обслуживает указанный город!")
