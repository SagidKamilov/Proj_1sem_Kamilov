print('1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление')
while True:
    try:
        a, b = float(input('Введите число А: ')), float(input('Введите число B (не равное 0): '))
        n = int(input('Введите цифру от 1 до 4: '))
        if 1 <= n <= 4:
            if b < 0:
                continue
            else:
                if n == 1:
                    v = a+b
                elif n == 2:
                    v = a-b
                elif n == 3:
                    v = a * b
                elif n == 4:
                    v = a / b
                print(v)
                break
        else:
            print('Вы ввели цифры вне указанного диапазона!Повторите ввод.')
            continue

    except ValueError:
        print('Введен неверный тип данных!')
        vari = input('Желаете попробовать еще раз? (x для выхода)')
        if vari.lower() == ' ':
            continue
        elif vari.lower() == 'x':
            break
