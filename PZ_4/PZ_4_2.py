# Выводит наименьшее из целых чисел K и сумму

try:  # Обработчик исключений
   a = float(input('Введите число A: '))
   if a > 1:  # Условие на проверку A > 1
       k = 1
       summa = 0
       while summa < a:  # Цикл, в котором рассчитывается сумма 1 + 1/2 + ... + 1/K
           summa += 1 / k
           k += 1
       print('\nСумма =', summa, '\nЧисло k =', k)
   else:
       print('Число A <= 1 !')
except ValueError:
   print('Введен неверный тип данных! Вводите число!')