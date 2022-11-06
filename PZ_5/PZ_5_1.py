# Программа для подсчета количества одинаковых цифр в четырехзначном числе

import random

def generate():
   number_in = random.randint(1000, 9999)  # Генерация случайного числа в диапазоне от 1000 до 9999
   # Блок с делением числа на цифры
   num1 = number_in // 1000
   num2 = number_in // 100 % 10
   num3 = number_in % 100 // 10
   num4 = number_in % 10
   check = 1
   # Ветки условий, в которых проверяются количество повторяющихся цифр
   if (num1 == num2) or (num1 == num3) or (num1 == num4):
       check += 1
   elif (num2 == num3) or (num2 == num4):
       check += 1
   elif num3 == num4:
       check += 1
   return 'Количество одинаковых цифр ' + str(check)


try:
    print(generate())
except TypeError:
    print('Аргументы не требуются')