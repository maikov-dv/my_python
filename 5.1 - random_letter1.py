# угадывание случайной буквы из слова

import random

word_list = ["самовар", "весна", "лето"]

word = random.choice(word_list)

letter = random.choice(word)

list_of_letters = list(word)

index_of_letter = list_of_letters.index(letter)

list_of_letters[index_of_letter] = "?"

new_word = "".join(list_of_letters)

print(new_word)

user_letter = input("Введите букву: ")

if user_letter == letter:
    print("Победа!\n", "Слово:", word)
else:
    print("Увы! Попробуйте в другой раз.\n", "Слово:", word)
