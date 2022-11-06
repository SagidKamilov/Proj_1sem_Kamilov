# Программа для подсчета количества монотонно убывающих участков

a = [3, 5, 92, 5, 100, 2, 50, 35, 79, 60, 98, 47, 92, 40, 32, 58, 24]


def compute(spisok):  # Функция считает количество участков с монотонным убыванием
    score = 0
    check_list = 0
    for i in range(len(spisok)):  # Цикл для перебора списка
        if spisok[i-1] < spisok[i]:  # Проверка на монотонность участка
            score += 1
        else:
            check_list += 1  # Здесь будет записывать колличество исключений, сработавших при проверке
    return 'Количество участков с монотонным убыванием: ' + str(check_list)


try:
    print(compute(a))  # Вызов функции
except TypeError:
    print('Нерправильный аргумент! Нужно передавать список!')