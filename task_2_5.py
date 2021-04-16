price_list = [57.8, 46.51, 97, 5.04, 189.78, 13.3, 1405, 28.01, 160.4, 493, 23.43, 74.09, 86.7]

# Задание А
for indx, price in enumerate(price_list):
    price_list[indx] = str(price).split('.')
    if len(price_list[indx]) == 2:
        price_list[indx][1] = f'{price_list[indx][1]:0<2}'
    else:
        price_list[indx].append('00')  #
    price_list[indx] = f'{price_list[indx][0]} руб {price_list[indx][1]} коп'
print(', '.join(price_list))

# Задание B
price_for_check = price_list[1]  # Выбираем элемент для проверки того, что он не изменится после сортировки.
print(f'id - {id(price_list[1])}')  # Смотрим id выбранного элемента
price_list.sort()
price_list.sort(key=len)
print(', '.join(price_list))
# Ищем элемент выбранный для проверки в уже отсортированном списке и выводим его id
print(f'id - {id(price_list[price_list.index(price_for_check)])}')

# Задание C
# price_list_reversed = price_list[::-1]  # для уже отсортированного по возрастанию списка
price_list_reversed = sorted(price_list, reverse=True)
price_list_reversed.sort(key=len, reverse=True)
print(', '.join(price_list_reversed))

# Задание D
price_list.sort()  # Для не отсортированного списка цен.
print(', '.join(sorted(price_list, key=len)[-5:]))
# print(', '.join(price_list[-5:]))  # Для уже отсортированного по возрастаню списка цен.
