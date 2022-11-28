'''Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая
средние температуры по месяцам в году. Преобразовать информацию из строки в
словарь, с использованием функции найти среднюю и минимальные температуры,
результаты вывести на экран.'''

info = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
info = info.split(' ')
info_dict = {}

for i in range(1, len(info)):  # Заполнение словаря значениями
    info_dict[i] = int(info[i])


def chis(dict_item):  # Функция для нахождения минимального и средного значений словаря
    list_item = [dict_item[d_item] for d_item in dict_item]
    mean_t = sum(list_item)/len(list_item)
    min_t = min(list_item)
    return mean_t, min_t


try:
    print('Среднее арифметическое:', chis(info_dict)[0], 'Минимальная темпа:', chis(info_dict)[1])
except TypeError:
    print('Ошибка с форматом данных!')