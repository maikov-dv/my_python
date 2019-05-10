# температура

with open('temper_stat.txt', 'r') as file:
    temp_list = []
    for temp in file:
        temp_num = float(temp.strip())
        temp_list.append(temp_num)
    
print('Максимальное значение:', max(temp_list))
print('Минимальное значение:', min(temp_list))
print('Средняя температура:', round((sum(temp_list)/len(temp_list)), 2))
print('Кол-во уникальный температур:', len(set(temp_list)))
