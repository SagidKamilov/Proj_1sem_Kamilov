# Вывод символов c1 и c2 n раз

try:  # Обработчик ошибок
    n = int(input('Сколько раз повторить выражение (> 0) N = : '))
    s = ''
    if n > 0:  # Проверка условия (N > 0)
        c1 = input('C1 = ')
        c2 = input('C2 = ')
        for i in range(n):  # цикл для сборки строки с указанными параметрами
            if i % 2 == 0:
                s += c1
            else:
                s += c2
        print('Выражение в итоге: ', s)
    else:
        print('N равен или меньше 0!')
except ValueError:
    print('Введите число!')
except TypeError:
    print('Неверный тип данных!')