import PySimpleGUI
import random


# нажатие на кнопку
def result():
    r = random.randint(1, 100)    # случайное число
    text_elem = window['-text-']    # текстовый элемент
    text_elem.update("AND THE RESULT IS: {}".format(r))    # вывод нового числа


# элементы окна
layout = [[PySimpleGUI.Button('RANDOMIZE, PLEASE!', enable_events=True, key='-func-', font='default')],
          [PySimpleGUI.Text('AND THE RESULT IS:', size=(25, 1), key='-text-', font='default')]]

# окно
window = PySimpleGUI.Window('RANDOM NUMBERS', layout, size=(290, 100))

# цикл
while True:
    event, values = window.read()
    if event in (PySimpleGUI.WIN_CLOSED, 'Exit'):   # если закрыть окно
        break
    if event == '-func-':   # если нажали на кнопку
        result()

window.close()
