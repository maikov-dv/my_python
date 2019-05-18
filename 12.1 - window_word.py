import tkinter
import random

def guess():
    if words[random_word] == entry.get():
        label_4.config(text = 'Угадали!')
    else:
        label_4.config(text = 'Не угадали!!!')

window = tkinter.Tk()

window.title('tk')

frame = tkinter.Frame(window)
frame.pack()

label_1 = tkinter.Label(frame, text ='Случайное слово:')
label_1.pack()

words = {'cat': 'кошка',
         'dog': 'собака',
         'bird': 'птица',
         'lion': 'лев',
         'elephant': 'слон'}

random_word = random.choice(list(words.keys()))

label_2 = tkinter.Label(frame, text = random_word)
label_2.pack()

label_3 = tkinter.Label(frame, text ='Укажите перевод слова:')
label_3.pack()

entry = tkinter.Entry(frame)
entry.pack()

label_4 = tkinter.Label(frame)
label_4.pack()

button_conv = tkinter.Button(frame, text='Готово!', command = guess) 
button_conv.pack()

button_exit = tkinter.Button(frame, text='Выход!', command = window.destroy) 
button_exit.pack()

window.mainloop()
