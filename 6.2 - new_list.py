initial_list = [2, 4, 9, 16, 25]

#1

new_list1 = []
for i in range(len(initial_list)):
    new_list1.append(pow(initial_list[i], 0.5))
print(new_list1)

#2

new_list2 = list(map((lambda y: pow(y, 0.5)), initial_list))
print(new_list2)

#3

new_list3 = [pow(initial_list[x], 0.5) for x in range(len(initial_list))]
print(new_list3)
