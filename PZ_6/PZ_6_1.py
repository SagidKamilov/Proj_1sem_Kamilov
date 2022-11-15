# Программа для вывода четных чисел по возрастанию и нечетных по убыванию в порядке индексов

spisok = [47, 64, 8, 85, 36, 32, 45, 5, 43, 63]


def go_back_out(spis):  # Функция с принятием аргумента списка
    print('Прямой вывод четных чисел: ')
    for i in range(len(spis)):  # цикл с выводом четных чисел их списка в порядке возрастания
        if spis[i] % 2 == 0:
            print(spis[i], end=' ')
    print('\n\nРеверсивный вывод нетных чисел:')
    for i in range((len(spis)-1), -1, -1):  # цикл в выводом нечетных чисел в порядке убывания
        if spis[i] % 2 != 0:
            print(spis[i], end=' ')


try:
    go_back_out(spisok)  # Вызов функции
except TypeError:
    print('Не правильный аргумент! Должен быть список')
