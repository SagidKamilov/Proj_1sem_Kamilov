# Программа для нахождения ближней точки b в множестве a

import random
import math

try:
    n = int(input('Размер множества a: '))
    a = [[random.randint(1, 100) for i in range(0, n)], [random.randint(1, 100) for i in range(0, n)]]  # Множество a
    b = [[], []] # Список для значений точки B
    s = [[100],[],[]]
    bx = int(input('Введите x B: '))
    by = int(input('Введите y B: '))
    b[0].append(bx)
    b[1].append(by)
    print(b)
    for i in range(0, n):
        r = math.sqrt((b[0][0]-a[0][i])**2+(b[1][0]-a[1][i])**2)
        if r < s[0][0]:
            s[0][0].clear()
            s[0].append(r)
            s[1].append(a[0][i])
            s[2].append(a[1][i])
    print(s)
except Exception as e:
    print('Вы ввели не целочисленный тип данных!', e)
