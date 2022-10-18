while True:
    try:
        a, b = int(input('Введите число a: ')), int(input('Введите число b: '))
        if (a % 2 != 0) or (b % 2 != 0):  # Проверка нечетности чисел
            print('Истина')
            break
        else:
            print('Ложь')
            continue
    except:
        print('Введен неверный тип данных!')
        vari = input('Желаете попробовать еще раз? (x для выхода)')
        if vari.lower() == ' ':
            continue
        elif vari.lower() == 'x':
            break
