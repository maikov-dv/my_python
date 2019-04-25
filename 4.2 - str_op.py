s = "У лукоморья 123 дуб зеленый 456"

#1

letter_in_string = s.find("я")

if letter_in_string == -1:
    print("Буква 'я' в строке НЕ встречается!")
else:
    print("Буква 'я' в строке встречается!")

print("Позиция (индекс) буквы 'я' в строке -", s.index("я"))

#2

print("Буква 'у' встречается", s.count("у"), "раз(а) в строке")

#3

consists_of_letters = s.isalpha()

if consists_of_letters == False:
    print(s.upper())
else:
    print("Строка состоит из букв")

#4

string_length = len(s)

if string_length > 4:
    print(s.lower())
else:
    print("Длина строки меньше 4 символов")

#5

print(s.replace("У", "О"))
