str_list = ['в', '5', 'часов', '17',
            'минут', 'температура', 'воздуха',
            'была', '+5', 'градусов']

new_str_list = []
for elem in str_list:  # Создаем новый список, добавляя необходимые кавычки и форматируя числовые элементы.
    if elem.isdigit():
        new_str_list.extend(['"', f'{int(elem):02}', '"'])
    elif elem[0] in ['+', '-']:
        if elem[1:].isdigit():
            new_str_list.extend(['"', f'{int(elem):+03}', '"'])
    else:
        new_str_list.append(elem)

print(' '.join(new_str_list))

'''
Склеиваем строку вручную, что бы избавиться от пробелов в кавычках.
'''
result_str = ''
for indx, elem in enumerate(new_str_list[:]):
    try:
        if (elem.isdigit() or elem[0] in ['+', '-'] and elem[1:].isdigit()) or elem == '"' and (new_str_list[indx+1].isdigit() or new_str_list[indx+1][0] in ['+', '-'] and new_str_list[indx+1][1:].isdigit()):
            result_str = f'{result_str}{elem}'
        else:
            result_str = f'{result_str}{elem} '
    except IndexError:
        continue
print(result_str)
